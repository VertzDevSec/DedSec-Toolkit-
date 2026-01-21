import os
import subprocess
import time
from colorama import Fore, init

init(autoreset=True)

# --- CONFIGURAÇÕES DE DEFESA ---
LIMITE_CONEXOES = 100  # Máximo de conexões por IP antes do bloqueio
INTERVALO_SCAN = 2     # Segundos entre cada verificação

def show_banner():
    os.system('clear')
    print(f"""
{Fore.CYAN}    ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗
{Fore.CYAN}    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
{Fore.WHITE}    ██║  ██║█████╗  ██║  ██║███████╗█████╗  ██║     
{Fore.WHITE}    ██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║     
{Fore.CYAN}    ██████╔╝███████╗██████╔╝███████║███████╗╚██████╗
{Fore.BLUE}             [ IPS - INTRUSION PREVENTION SYSTEM ]
{Fore.YELLOW}    --------------------------------------------------
    """)

def aplicar_bloqueio(ip):
    """ Aplica a regra de DROP no iptables para o IP agressor """
    print(f"{Fore.RED}[!!!] ALERTA: Ataque detectado vindo de {ip}")
    print(f"{Fore.YELLOW}[*] Aplicando bloqueio de Kernel (iptables DROP)...")
    
    # Comando para inserir a regra de bloqueio no topo da lista (Index 1)
    os.system(f"sudo iptables -I INPUT -s {ip} -j DROP")
    print(f"{Fore.GREEN}[SUCCESS] IP {ip} mitigado com sucesso.")

def monitorar_trafego():
    print(f"{Fore.WHITE}[*] Monitorando conexões ativas... (Limite: {LIMITE_CONEXOES} Sockets)")
    
    while True:
        try:
            # Comando SS para contar conexões por IP
            cmd = "ss -antu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c"
            output = subprocess.check_output(cmd, shell=True).decode()
            
            linhas = output.strip().split('\n')
            for linha in linhas:
                if not linha.strip(): continue
                
                partes = linha.split()
                if len(partes) < 2: continue
                
                qtd_conexoes = int(partes[0])
                ip_origem = partes[1]

                # Ignora o localhost e IPs vazios
                if ip_origem in ["127.0.0.1", "0.0.0.0", "Address", ""]: continue

                if qtd_conexoes > LIMITE_CONEXOES:
                    aplicar_bloqueio(ip_origem)
                    # Aguarda um pouco para evitar loops infinitos de bloqueio
                    time.sleep(5)
            
            time.sleep(INTERVALO_SCAN)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Desativando Guardian. Limpando regras de firewall...")
            os.system("sudo iptables -F") # Limpa todas as regras ao sair
            break

if __name__ == "__main__":
    show_banner()
    # Ativa Proteções Base antes de iniciar o monitoramento
    print(f"{Fore.BLUE}[*] Ativando Proteção de Kernel (SYN Cookies)...")
    os.system("sudo sysctl -w net.ipv4.tcp_syncookies=1 > /dev/null")
    
    monitorar_trafego()