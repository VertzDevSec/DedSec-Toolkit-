from scapy.all import sniff
import os
import time
import sys
import signal
from colorama import Fore, Style, init

# Inicialização visual
init(autoreset=True)

packet_count = 0
start_time = time.time()

def show_monitor_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{Fore.GREEN}    ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗
{Fore.GREEN}    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
{Fore.WHITE}    ██║  ██║█████╗  ██║  ██║███████╗█████╗  ██║     
{Fore.WHITE}    ██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║     
{Fore.GREEN}    ██████╔╝███████╗██████╔╝███████║███████╗╚██████╗
{Fore.GREEN}    ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝
{Fore.WHITE}             NETWORK TELEMETRY - SENSOR ATIVO
    
{Fore.CYAN}    [+] Create by: VertzDevSec (DedSec Security)
{Fore.GREEN}    [+] Operation: Traffic Analysis
{Fore.GREEN}    [+] Mode: Real-time Packet Capture
{Fore.YELLOW}    ----------------------------------------------------------------------
    """)
def monitor_callback(pkt):
    global packet_count
    packet_count += 1
    
    elapsed = time.time() - start_time
    if elapsed > 1:
        pps = packet_count / elapsed
        bars = "█" * min(int(pps / 50), 20)
        
        sys.stdout.write(
            f"\r{Fore.WHITE}[{Fore.CYAN}AO VIVO{Fore.WHITE}] "
            f"{Fore.GREEN}PPS: {pps:.2f} {Fore.WHITE}| "
            f"{Fore.YELLOW}Total de Pacotes: {packet_count} {Fore.WHITE}| "
            f"{Fore.CYAN}Carga: {bars:<20}"
        )
        sys.stdout.flush()
        
def panic_button(sig, frame):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{Fore.RED}[!] BOTÃO DE PÂNICO ATIVADO - Sessão Encerrada.")
    print(f"{Fore.WHITE}Relatório Final: {packet_count} pacotes interceptados.")
    print(f"\n{Fore.GREEN}A DedSec lhe deu a verdade. Faça o que desejar.")
    print(f"{Fore.WHITE}Junte-se a nós. Somos DedSec. {Fore.RED}Não perdoamos. Não esquecemos.")
    sys.exit(0)

# Configura o sinal de interrupção (Ctrl+C)
signal.signal(signal.SIGINT, panic_button)

def start_monitor():
    show_monitor_banner()
    print(f"{Fore.YELLOW}[*] Escaneando tráfego na interface principal...")
    print(f"{Fore.RED}[!] Certifique-se de que o VS Code está como ADMINISTRADOR.\n")
    
    try:
        sniff(prn=monitor_callback, store=0)
    except Exception as e:
        print(f"\n{Fore.RED}[X] ERRO CRÍTICO: Falha ao acessar drivers de rede.")
        print(f"{Fore.WHITE}Verifique se o Npcap está instalado no seu Windows.")

if __name__ == "__main__":
    try:
        start_monitor()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW} ----------------------------------------------------------------------")
        print(f"{Fore.CYAN}  [!] Sessão encerrada.")
        print(f"{Fore.WHITE}  Relatório: {packet_count} pacotes interceptados.")
        print(f"\n{Fore.GREEN}  A DedSec lhe deu a verdade. Faça o que desejar.")
        print(f"{Fore.WHITE}  Junte-se a nós. Somos DedSec. {Fore.RED}Não perdoamos. Não esquecemos.")
        print(f"{Fore.YELLOW} ----------------------------------------------------------------------\n")
        sys.exit()