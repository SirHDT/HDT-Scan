# HDT Scan

This is a Python program that automates the execution of various network scanning tool commands, such as rustscan, nmap, and gobuster. It simplifies the process of vulnerability assessment and information discovery on a specific target.

## Prerequisites

Make sure you have the following tools installed on your system:

- RustScan
- Nmap
- Gobuster

## How to Use

1. Clone this repository:
```
git clone https://github.com/SirHDT/HDT-Scan.git
```
2. Navigate to the project directory:
```
cd HDT-Scan
```
3. Run the Python script:
```
python HDT-Scan
```
4. Follow the instructions provided in the console to input the target IP and ports (if required).

## Functions

- rustscan(target, ports): Conducts a fast port scan using RustScan.
- nmap_scan(target): Performs a port and service scan on the specified target using Nmap.
- gobuster(target, port, wordlist): Performs directory and file enumeration on a web server using Gobuster.

## Example Usage

```
HDT Scan!
Target IP: 172.???.???.???
# rustscan(target)

Ports: 22,80,445,????
# nmap_scan(target, ports)

Web Port: 80
Enter Custom wordlist path: /usr/share/wordlist/???
# gobuster(target, port, wordlist)
```

## Notes

- Make sure you have sufficient permissions to execute these commands, especially if you're running the script in a Linux environment.
- This tool is intended for educational and ethical penetration testing purposes only. Make sure to use it in compliance with local laws and obtain authorization before conducting security scans on systems you don't own.
- Always use with caution and responsibility. The author is not responsible for any illegal use of this tool.

---

Feel free to contribute improvements or report issues by opening an issue or sending a pull request. Your contribution is appreciated!
