# 🛡️ DedSec Network Toolkit `v3.0`

> **Status da Missão:** Operacional (Laboratório de Redes)  
> **Desenvolvedor:** VertzDevSec  
> **Plataforma:** Python 3.x (Ambiente Windows/Linux)

Este toolkit foi projetado para demonstrar o impacto de ataques de **Exaustão de Recursos (Camada 7)** e fornecer auditoria forense detalhada através de telemetria em tempo real.

---

## 🚀 Funcionalidades de Elite

- [x] **📊 Gráfico de Impacto:** Visualização em barras ASCII da dominância de protocolos.
- [x] **🌐 Auditoria Ampliada:** Rastreamento das 10 maiores origens de tráfego.
- [x] **💾 Volumetria Real:** Cálculo de tráfego capturado em Megabytes (MB).
- [x] **🤖 Camuflagem Bot-Referer:** Simulação de requisições via Google, Facebook e Bing.
- [x] **⚡ Port Randomization:** Alternância dinâmica de portas de origem para bypass de filtros.

---

## 📦 Bibliotecas Necessárias

Biblioteca,Finalidade
Scapy: Captura e decodificação de pacotes brutos (Sniffing).
Tabulate: Geração de tabelas profissionais e gráficos de barras no terminal.
Colorama: Interface visual colorida para alertas de latência.

Para manter o visual organizado e o funcionamento correto, instale as dependências oficiais:

```bash
pip install scapy tabulate colorama

🛠️ Guia de Operação
1. Preparação do Ambiente
Certifique-se de que os arquivos abaixo estão na mesma pasta:

DedSec_DDoS.py (Motor de Estresse)

DedSec_Sniffer.py (Sensor de Telemetria)

headers.txt (Lista de Agentes de Navegação)

2. Monitoramento (Telemetry)
Sempre inicie o monitor primeiro. No Windows, utilize o terminal como Administrador.

PowerShell

python DedSec_Sniffer.py
Informe o IP do alvo e aguarde o início da captura.

3. Operação de Estresse (DDoS)
Em uma janela separada, dispare o ataque:

PowerShell

python DedSec_DDoS.py
Credenciais: Usuário: dedsec | Senha: dedsec.

📑 Modelo de Relatório Final
Ao encerrar o monitoramento com Ctrl+C, o sistema gera automaticamente uma auditoria formatada:

Plaintext

╔══════════════╦═══════════════╦════════════╦════════════╗
║ Protocolo    ║ Qtd Pacotes   ║ Percentual ║ Gráfico    ║
╠══════════════╬═══════════════╬════════════╬════════════╣
║ TCP (HTTP)   ║ 25.420        ║ 92.5%      ║ █████████  ║
╚══════════════╩═══════════════╩════════════╩════════════╝
⚠️ Aviso Legal
Este software foi desenvolvido exclusivamente para fins de estudo acadêmico em ambientes controlados. O desenvolvedor não se responsabiliza pelo uso indevido da ferramenta.

Join us. Join DedSec.
