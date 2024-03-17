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
    if system == 'Linux':
        print("Detected Linux OS.")
        with open('/etc/os-release', 'r') as f:
            os_info = f.readlines()
            version = next((line.split('=')[1].strip('"') for line in os_info if line.startswith('VERSION_ID')), None)
            if version == '20.04':
                install_command = 'sudo apt-get install openjdk-11-jdk -y'  # For Ubuntu 20.04 LTS
            else:
                install_command = 'sudo yum install java-11-amazon-corretto.x86_64 -y'  # For other Linux distributions including Amazon Linux
    elif system == 'Darwin':
        print("Detected macOS.")
        install_command = '/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" && brew install adoptopenjdk11'
        # Install Homebrew for macOS if not already installed and then install adoptopenjdk
    else:
        print("Java installation for Windows is not supported.")
        return

    try:
        subprocess.run(install_command, shell=True, check=True)
        print("Java installation successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing Java: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_java()
