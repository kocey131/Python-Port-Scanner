import socket
import threading
from datetime import datetime

cible = input('Cible IP ou localhost:')
port_debut = 0
port_fin = 65535
ports_ouverts = []

def ports_scan(cible, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        r = s.connect_ex((cible, port))
        if r == 0:
            print(f"Port {port} est ouvert.")
            ports_ouverts.append(port)
        else:
            print(f"Port {port} est fermé.")

def scanner_ports(cible, port_debut, port_fin):
    debut_scan = datetime.now()
    threads = []
    for port in range(port_debut, port_fin + 1):
        thread = threading.Thread(target=ports_scan, args=(cible, port))
        threads.append(thread)
        thread.daemon = True
        thread.start()

    
    for thread in threads:
        thread.join()

    duree_scan = datetime.now() - debut_scan
    print(f"Scan terminer. Ports ouverts : {ports_ouverts} Durée: {duree_scan}.")

scanner_ports(cible, port_debut, port_fin)
