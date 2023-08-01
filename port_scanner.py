import socket
import re

# Setting up socket
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.settimeout(5)

try:
    # Getting target IP
    IP = input("Target IP : ")
    
    # Validating IP address
    if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', IP):
        raise ValueError("Invalid IP address")

    # Getting target port
    Port = int(input("Port : "))
    
    # Validating port number
    if Port < 0 or Port > 65535:
        raise ValueError("Invalid port number")

    # Connecting to the target
    R = S.connect_ex((IP, Port))
    S.close()

    # Printing scan result
    service = socket.getservbyport(Port)
    print('________________________________')
    
    if R == 0:
        print(f"Target IP: {IP}\nPort: {Port}\nStatus: Open\nService: {service}")
    else:
        print(f"Target IP: {IP}\nPort: {Port}\nStatus: Closed\nService: {service}")

except ValueError as e:
    print(f"Error: {e}")
except socket.gaierror as e:
    print(f"Address-related error: {e}")
except socket.timeout:
    print("Connection timed out")
except socket.error as e:
    print(f"Socket error: {e}")
