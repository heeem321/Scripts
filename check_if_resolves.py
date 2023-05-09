import socket
import sys

# Get the list of domains from the command line arguments
domains = sys.argv[1:]

# Loop through each domain and check if it resolves
for domain in domains:
    try:
        # Use the gethostbyname function to get the IP address for the domain
        ip = socket.gethostbyname(domain)
        print(f"{domain} resolves to {ip}")
    except socket.gaierror:
        # If the domain doesn't resolve, print an error message
        print(f"{domain} does not resolve")

# Usage for domain in $(cat domains); do python3 {script_name} $domain; done;
