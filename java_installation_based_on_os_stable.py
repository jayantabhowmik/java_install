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
        os_info = {}
        with open('/etc/os-release', 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    os_info[key] = value.strip('"')

        if 'ID' in os_info:
            os_id = os_info['ID'].lower()
            if os_id == 'ubuntu':
                install_command = 'sudo apt-get install openjdk-11-jdk -y'
            elif os_id == 'debian':
                install_command = 'sudo apt install default-jre -y'
            elif os_id == 'rhel':
                install_command = 'sudo yum install java-11-openjdk.x86_64 -y'
            elif os_id == 'fedora':
                install_command = 'sudo dnf install java-11-openjdk.x86_64 -y'
            elif os_id == 'centos':
                install_command = 'sudo yum install java-11-openjdk.x86_64 -y'
            elif os_id == 'amzn':
                install_command = 'sudo yum install java-11-amazon-corretto.x86_64 -y'
            else:
                print("Unsupported Linux distribution.")
                return
        else:
            print("Failed to detect Linux distribution.")
            return
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
