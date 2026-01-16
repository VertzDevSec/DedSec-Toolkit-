import time
import threading
import subprocess
import platform
import os
from scapy.all import sniff
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Variáveis globais para sincronização entre threads
pacotes_contados = 0
latencia_atual = "Iniciando..."

def show_monitor_banner():
    """Banner personalizado VertzDevSec para o Monitor."""
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

def contar_pacotes(pkt):
    global pacotes_contados
    pacotes_contados += 1

def obter_latencia(alvo):
    """Thread dedicada para medir o ping sem travar o contador principal."""
    global latencia_atual
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    timeout_param = '-w' if platform.system().lower() == 'windows' else '-W'
    
    while True:
        try:
            inicio = time.time()
            # Envia 1 pacote de ping com timeout de 2 segundos
            processo = subprocess.run(
                ['ping', param, '1', timeout_param, '2000', alvo],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            fim = time.time()
            
            if processo.returncode == 0:
                ms = (fim - inicio) * 1000
                latencia_atual = f"{ms:.2f} ms"
            else:
                latencia_atual = "TIMEOUT / QUEDA"
        except:
            latencia_atual = "ERRO DE REDE"
        
        time.sleep(1)

def monitor_display():
    """Thread para atualizar os dados de telemetria no terminal."""
    global pacotes_contados
    while True:
        pps = pacotes_contados
        pacotes_contados = 0 
        
        # Lógica de cores baseada na performance da rede
        cor_ms = Fore.GREEN
        try:
            valor_ms = float(latencia_atual.split()[0])
            if valor_ms > 150: cor_ms = Fore.YELLOW
            if valor_ms > 800: cor_ms = Fore.RED
        except:
            if "TIMEOUT" in latencia_atual: cor_ms = Fore.RED

        # Exibe os dados formatados
        info = f"{Fore.WHITE}[TELEMETRIA] {Fore.CYAN}PPS: {Fore.YELLOW}{pps:5} {Fore.WHITE}| {Fore.CYAN}LATÊNCIA: {cor_ms}{latencia_atual:15}"
        print(f"\r{info}", end="", flush=True)
        time.sleep(1)

# --- INÍCIO DO PROGRAMA ---
show_monitor_banner()

# Solicita o alvo para monitorar (Ex: o gateway do roteador antigo)
alvo_ping = input(f"{Fore.CYAN}[?] Digite o IP do Alvo para monitorar Latência: ").strip()

# Inicializa as threads de monitoramento
threading.Thread(target=obter_latencia, args=(alvo_ping,), daemon=True).start()
threading.Thread(target=monitor_display, daemon=True).start()

print(f"\n{Fore.GREEN}[*] Sniffer Ativo. Analisando pacotes via Scapy...\n")

try:
    # O store=0 é fundamental para não travar a memória RAM da sua máquina durante o teste
    sniff(prn=contar_pacotes, store=0)
except KeyboardInterrupt:
    print(f"\n\n{Fore.RED}[!] Telemetria encerrada.")
