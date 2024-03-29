import pygame
import dlib
from scipy.spatial import distance

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Eye Tracking Keyboard")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Define font
font = pygame.font.SysFont(None, 36)

# Define keyboard layout
keyboard_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
    ['Space', 'Delete']
]

# Define key sizes and positions
KEY_WIDTH = SCREEN_WIDTH // 12
KEY_HEIGHT = SCREEN_HEIGHT // 8
KEY_MARGIN = 5

# Initialize dlib's face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Function to calculate eye aspect ratio (EAR)
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Function to detect blinks
def detect_blink(shape):
    left_eye = [shape.part(i) for i in range(36, 42)]
    right_eye = [shape.part(i) for i in range(42, 48)]

    left_ear = eye_aspect_ratio(left_eye)
    right_ear = eye_aspect_ratio(right_eye)

    ear_threshold = 0.2  # Adjust as needed
    if left_ear < ear_threshold and right_ear < ear_threshold:
        return True
    else:
        return False

# Function to draw keyboard
def draw_keyboard(selected_key):
    for y, row in enumerate(keyboard_layout):
        for x, key in enumerate(row):
            key_rect = pygame.Rect(x * (KEY_WIDTH + KEY_MARGIN), y * (KEY_HEIGHT + KEY_MARGIN),
                                    KEY_WIDTH, KEY_HEIGHT)
            if key == selected_key:
                pygame.draw.rect(screen, RED, key_rect)
            else:
                pygame.draw.rect(screen, GRAY, key_rect)
            text_surface = font.render(key, True, BLACK)
            text_rect = text_surface.get_rect(center=key_rect.center)
            screen.blit(text_surface, text_rect)

# Main loop
def main():
    selected_key = ''
    running = True
    while running:
        screen.fill(WHITE)
        draw_keyboard(selected_key)
        pygame.display.flip()
        
        # Detecting blinks and selecting key
        frame = pygame.surfarray.array3d(screen)
        gray = pygame.surfarray.array3d(screen)
        rects = detector(gray, 0)

        for rect in rects:
            shape = predictor(gray, rect)
            if detect_blink(shape):
                selected_key = keyboard_layout[1][0]  # For example, select the first key in the second row
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
