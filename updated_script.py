import platform
import subprocess
import sys

def check_java_installed():
    try:
        subprocess.run('java -version', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_java():
    if check_java_installed():
        print("Java is already installed.")
        return

    system = platform.system()
    if system == 'Windows':
        print("Detected Windows OS.")
        install_command = 'choco install adoptopenjdk -y'  # Assuming you have Chocolatey installed for Windows
    elif system == 'Linux':
        print("Detected Linux OS.")
        install_command = 'sudo apt-get install default-jdk -y'  # For Ubuntu/Debian based systems
    elif system == 'Darwin':
        print("Detected macOS.")
        install_command = '/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" && brew install adoptopenjdk'
        # Install Homebrew for macOS if not already installed and then install adoptopenjdk
    else:
        print("Unsupported operating system.")
        return

    try:
        subprocess.run(install_command, shell=True, check=True)
        print("Java installation successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing Java: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_java()

