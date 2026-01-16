import time
import threading
import subprocess
import platform
import os
import re
import sys
from scapy.all import sniff, IP, TCP, UDP, ICMP
from colorama import Fore, init
from tabulate import tabulate

init(autoreset=True)

# --- VARIÁVEIS DE ESTATÍSTICA ---
pacotes_contados = 0
total_bytes = 0
latencia_atual = "Iniciando..."
resumo_trafego = {"TCP": 0, "UDP": 0, "ICMP": 0, "Outros": 0}
ips_origem = {}
deve_parar = False

def show_monitor_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{Fore.GREEN}    ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗
{Fore.GREEN}    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
{Fore.WHITE}    ██║  ██║█████╗  ██║  ██║███████╗█████╗  ██║     
{Fore.WHITE}    ██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║     
{Fore.GREEN}    ██████╔╝███████╗██████╔╝███████║███████╗╚██████╗
{Fore.GREEN}    ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝
{Fore.WHITE}             NETWORK TELEMETRY - SENSOR ATIVO V3.0
    
{Fore.CYAN}    [+] Author: VertzDevSec | Lab: Faculdade de Cibersegurança
{Fore.GREEN}    [+] Análise: Volumetria (MB) e Gráficos de Impacto
{Fore.YELLOW}    ----------------------------------------------------------------------
    """)

def contar_pacotes(pkt):
    global pacotes_contados, resumo_trafego, ips_origem, total_bytes
    pacotes_contados += 1
    total_bytes += len(pkt)
    if pkt.haslayer(IP):
        src_ip = pkt[IP].src
        ips_origem[src_ip] = ips_origem.get(src_ip, 0) + 1
        if pkt.haslayer(TCP): resumo_trafego["TCP"] += 1
        elif pkt.haslayer(UDP): resumo_trafego["UDP"] += 1
        elif pkt.haslayer(ICMP): resumo_trafego["ICMP"] += 1
        else: resumo_trafego["Outros"] += 1

def verificar_parada(pkt):
    return deve_parar

def imprimir_relatorio_final():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{Fore.YELLOW}="*70)
    print(f"{Fore.WHITE}             DEDSEC FORENSICS - RELATÓRIO FINAL DE IMPACTO")
    print(f"{Fore.YELLOW}="*70)
    
    total_mb = total_bytes / (1024 * 1024)
    total_pkts = sum(resumo_trafego.values())
    
    # Gerando Tabela de Protocolos com Gráfico de Barras
    dados_proto = []
    for k, v in resumo_trafego.items():
        porcentagem = (v / total_pkts * 100) if total_pkts > 0 else 0
        barra = "█" * int(porcentagem / 5) # 1 bloco para cada 5%
        dados_proto.append([k, v, f"{porcentagem:.1f}%", f"{Fore.GREEN}{barra}"])

    print(f"\n{Fore.CYAN}📊 ANÁLISE DE TRÁFEGO POR PROTOCOLO:")
    print(tabulate(dados_proto, headers=["Protocolo", "Qtd Pacotes", "Percentual", "Gráfico"], tablefmt="fancy_grid"))
    
    # Top 10 Origens
    print(f"\n{Fore.CYAN}🌐 AUDITORIA DE ORIGEM (TOP 10 IPS):")
    top_ips = sorted(ips_origem.items(), key=lambda x: x[1], reverse=True)[:10]
    print(tabulate(top_ips, headers=["Endereço IP", "Total de Pacotes"], tablefmt="psql"))
    
    print(f"\n{Fore.WHITE}MÉTRICAS TÉCNICAS:")
    print(f"{Fore.GREEN}[>] VOLUME TOTAL CAPTURADO: {Fore.YELLOW}{total_mb:.2f} MB")
    print(f"{Fore.GREEN}[>] ESTADO DO GATEWAY: {Fore.RED if 'TIMEOUT' in latencia_atual else Fore.GREEN}{latencia_atual}")
    print(f"\n{Fore.CYAN}[+] Relatório gerado para fins de documentação acadêmica.\n")

def obter_latencia(alvo):
    global latencia_atual
    p = '-n' if platform.system().lower() == 'windows' else '-c'
    w = '-w' if platform.system().lower() == 'windows' else '-W'
    while True:
        try:
            start = time.time()
            proc = subprocess.run(['ping', p, '1', w, '2000', alvo], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            latencia_atual = f"{(time.time()-start)*1000:.2f} ms" if proc.returncode == 0 else "TIMEOUT / QUEDA"
        except: latencia_atual = "ERRO"
        time.sleep(1)

def monitor_display():
    global pacotes_contados
    while True:
        pps = pacotes_contados
        pacotes_contados = 0
        cor = Fore.GREEN if "ms" in latencia_atual else Fore.RED
        sys.stdout.write(f"\r{Fore.WHITE}[TELEMETRIA] {Fore.CYAN}PPS: {Fore.YELLOW}{pps:5} {Fore.WHITE}| {Fore.CYAN}LATÊNCIA: {cor}{latencia_atual:15}")
        sys.stdout.flush()
        time.sleep(1)

if __name__ == "__main__":
    show_monitor_banner()
    alvo = input(f"{Fore.CYAN}[?] Digite o IP do Alvo para telemetria: ").strip()
    threading.Thread(target=obter_latencia, args=(alvo,), daemon=True).start()
    threading.Thread(target=monitor_display, daemon=True).start()
    try:
        sniff(prn=contar_pacotes, store=0, stop_filter=verificar_parada)
    except KeyboardInterrupt:
    
        deve_parar = True
        print(f"\n\n{Fore.RED}[!] Interrupção detectada. Compilando dados..."); time.sleep(1.5)
    finally:
        imprimir_relatorio_final()

