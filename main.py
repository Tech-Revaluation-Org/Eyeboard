import subprocess

def run_module():
    try:
        # Change directory to the "modiule" directory
        subprocess.run("cd modiule", shell=True, check=True)
        
        # Run the module
        subprocess.run("python eyeboard.py", shell=True, check=True)
        
    except subprocess.CalledProcessError as e:
        print("Error:", e)

if __name__ == "__main__":
    run_module()
