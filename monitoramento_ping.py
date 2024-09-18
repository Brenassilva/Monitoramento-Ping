import os
import platform

def ping_host(host):
    # Comando para pingar o host, dependendo do sistema operacional
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    # Executa o ping
    command = f"ping {param} 1 {host}"
    response = os.system(command)
    
    # Verifica se o host está acessível
    if response == 0:
        print(f"{host} está online.")
    else:
        print(f"{host} está offline ou inacessível.")

# Lista de hosts para monitorar
hosts = ["8.8.8.8", "192.168.0.1", "www.google.com"]

# Pingar cada host na lista
for host in hosts:
    ping_host(host)
