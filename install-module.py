import os
import subprocess
import sys

def create_virtualenv(venv_dir='venv'):
    if not os.path.exists(venv_dir):
        print("[+] Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    else:
        print("[+] Virtual environment already exists.")

def install_requirements(venv_dir='venv'):
    pip_executable = os.path.join(venv_dir, 'Scripts' if os.name == 'nt' else 'bin', 'pip')

    print("[+] Installing required packages...")
    subprocess.check_call([pip_executable, "install", "--upgrade", "pip"])
    subprocess.check_call([pip_executable, "install", "-r", "requirements.txt"])

def write_requirements_file():
    requirements = [
        "PyQt5>=5.15.0",
        "psutil>=5.9.0",
        "requests>=2.28.0"
    ]
    with open("requirements.txt", "w") as f:
        f.write("\n".join(requirements))
    print("[+] requirements.txt written.")

if __name__ == "__main__":
    write_requirements_file()
    create_virtualenv()
    install_requirements()
    print("[✓] Setup complete. To activate the environment:")
    if os.name == "nt":
        print("    venv\\Scripts\\activate")
    else:
        print("    source venv/bin/activate")

