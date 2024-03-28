import subprocess
import os

def nmap_scan(target, ports):
    try:
        # Execute the nmap command
        result = subprocess.run(['nmap', '-sV', '-p', ports, target], capture_output=True, text=True)
        # Display the command output
        print("Nmap Output:")
        print(result.stdout)
    except FileNotFoundError:
        print("Nmap not found. Please install Nmap on your system.")
    except subprocess.CalledProcessError as error:
        print(f"Error: Nmap command failed with return code {error.returncode}.")
        print("Output:", error.output)

def rustscan(target):
    try:
        # Execute the rustscan command
        process = subprocess.Popen(['rustscan', '-b', '2000', '-a', target, '-u' '1900'], stdout=subprocess.PIPE, text=True)
        # Display the output in real-time while the process is running
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
        
        # Wait for the process to finish and get the return code
        process.wait()
    except FileNotFoundError:
        print("Rustscan not found. Please install Rustscan on your system.")

def gobuster(target, port, wordlist):
    try:
        # Execute the gobuster command
        proc = subprocess.Popen(['gobuster', 'dir', '-u', f'http://{target}:{port}', '-w', wordlist], stdout=subprocess.PIPE, text=True)
        # Display the output in real-time while the process is running
        while True:
            output = proc.stdout.readline()
            if output == '' and proc.poll() is not None:
                break
            if output:
                print(output.strip())
        
        # Wait for the process to finish and get the return code
        proc.wait()
    except FileNotFoundError:
        print("Gobuster not found. Please install Gobuster on your system.")

def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'y' or user_input == 'n':
            return user_input
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def is_valid_path(path):
    # Check if the given path exists.
    return os.path.exists(path)

def get_wordlist_path():
    while True:
        wordlist_path = input("Enter custom wordlist path: ").strip()
        if os.path.exists(wordlist_path):
            print("Wordlist path is valid.")
            return wordlist_path
        else:
            print("Error: Wordlist path does not exist.")

def main():
    try:
        print("HDT Scan!")
        target = input("Target IP: ")
        rustscan(target)
        skip_nmap = get_valid_input("Do you want to skip Nmap scan and proceed directly to Gobuster? (Y/N): ")
        if not skip_nmap:
            ports = input("Ports: ")
            nmap_scan(target, ports)
        port = input("Web Port: ")
        wordlist = get_wordlist_path()
        print("Wordlist path:", wordlist)
        gobuster(target, port, wordlist)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit(1)
    except Exception as e:
        print("An unexpected error occurred:", e)
        exit(1)

if __name__ == "__main__":
    main()
