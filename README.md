# Eyeboard

## About
Eyeboard is a virtual keyboard implementation that allows users to type using eye movements. It utilizes eye tracking technology to detect blinks and select keys on a virtual keyboard displayed on the screen.

## How it Works
Eyeboard works by continuously monitoring the user's eyes using a webcam or other compatible eye tracking device. It detects blinks using dlib's facial landmark detection and calculates the eye aspect ratio (EAR) to determine if a blink has occurred. When a blink is detected, the corresponding key on the virtual keyboard is selected, allowing the user to input text without physical keystrokes.

## Installation
To run Eyeboard, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Tech-Now-Org/Eyeboard.git
   ```

2. Navigate to the Eyeboard directory:
   ```bash
   cd Eyeboard
   ```

3. Install the required dependencies:
   ```bash
   pip install pygame dlib scipy
   ```

4. Download the pre-trained facial landmark predictor file (`shape_predictor_68_face_landmarks.dat`) from the dlib website or use a custom trained model.

5. Run the main.py script to start Eyeboard:
   ```bash
   python main.py
   ```

## Usage
To use Eyeboard, follow these steps:

1. Ensure your webcam or eye tracking device is connected and positioned correctly.

2. Run the Eyeboard application using the installation instructions provided above.

3. Look at the virtual keyboard displayed on the screen.

4. Blink to select keys on the virtual keyboard and input text.

## Contributing
Contributions to Eyeboard are welcome! Here's how you can contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature`)
3. Make changes and commit them (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature`)
5. Create a new Pull Request

## License
Eyeboard is licensed under the [MIT License](LICENSE).

## Credits
Eyeboard is developed and maintained by Tech Now Org.

## Support
For support or assistance, please contact [Tech Now Org](https://github.com/Tech-Now-Org).

---

Feel free to customize the content and structure of the README to fit the specific features and usage of the Eyeboard technology!
