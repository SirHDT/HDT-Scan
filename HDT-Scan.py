import subprocess

def nmap_scan(target, ports):
    try:
        # Execute the nmap command
        result = subprocess.run(['nmap', '-sV', '-p', ports, target], capture_output=True, text=True)
        # Display the command output
        print("Nmap Output:")
        print(result.stdout)
    except FileNotFoundError:
        print("Nmap not found. Please install Nmap on your system.")

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

def main():
    print("HDT Scan!")
    target = input("Target IP: ")
    rustscan(target)
    skip_nmap = input("Do you want to skip Nmap scan and proceed directly to Gobuster? (Y/N): ").lower() == 'y'
    if not skip_nmap:
        ports = input("Ports: ")
        nmap_scan(target, ports)
    port = input("Web Port: ")
    wordlist = input("Enter custom wordlist path: ")
    gobuster(target, port, wordlist)

if __name__ == "__main__":
    main()
