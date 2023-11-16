import socket

def ip_to_domain(ip_address):
    try:
        return socket.gethostbyaddr(ip_address)[0]
    except (socket.herror, socket.gaierror) as e:
        return f"Error: {e}"

def domain_to_ip(domain_name):
    try:
        return socket.gethostbyname(domain_name)
    except (socket.gaierror, socket.herror) as e:
        return f"Error: {e}"

while True:
    print("1. IP to Domain Lookup")
    print("2. Domain to IP Lookup")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        ip_address = input("Enter an IP address: ")
        result = ip_to_domain(ip_address)
        print(f"Domain associated with {ip_address}: {result}")
    elif choice == '2':
        domain_name = input("Enter a domain name (URL): ")
        result = domain_to_ip(domain_name)
        print(f"IP address associated with {domain_name}: {result}")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

