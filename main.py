import socket
import threading
from datetime import datetime
import dns.resolver

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Get the domain name or IP address from the user
input_value = input('IP or domaine name: ').strip()

# Resolve the domain name to an IP address if necessary
if is_valid_ip(input_value) or input_value == "localhost":
    cible = input_value
else:
    try:
        result = dns.resolver.resolve(input_value, 'A')
        cible = result[0].to_text()
        print(f"{input_value} Resolved to {cible}")
    except (dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.resolver.NoAnswer) as e:
        print(f"Error in DNS name resolution : {e}")
        exit(1)

port_debut = 0
port_fin = 1023  # Default to scanning well-known [makes the process faster]
ports_ouverts = []
ports_ouverts_lock = threading.Lock()

def ports_scan_digit(cible, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        r = s.connect_ex((cible, port))
        with ports_ouverts_lock:
            if r == 0:
                ports_ouverts.append(port)
                print(f"Port {port} is open.")
            else:
                print(f"Port {port} is closed.")

def scanner_ports_digit(cible, port_debut, port_fin):
    debut_scan = datetime.now()
    threads = []
    for port in range(port_debut, port_fin + 1):
        thread = threading.Thread(target=ports_scan_digit, args=(cible, port))
        threads.append(thread)
        thread.daemon = True
        thread.start()

    for thread in threads:
        thread.join()

    duree_scan = datetime.now() - debut_scan
    print(f"Scan done. Open Ports : {ports_ouverts} Durée: {duree_scan}.")

scanner_ports_digit(cible, port_debut, port_fin)
