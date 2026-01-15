# DedSec Toolkit - Versão de Laboratório 🛠️

Este repositório contém ferramentas de estudo desenvolvidas para testes de estresse e monitoramento de rede em ambientes controlados. O projeto foi criado para ajudar estudantes de cibersegurança a entenderem a resiliência de servidores e o comportamento de protocolos de rede.

## 🚀 Ferramentas Incluídas

1. **DedSec_DDoS.py**: Script de teste de carga (DDoS) utilizando a técnica de *HTTP Pipelining* para simular tráfego massivo.

2. **DedSec_Sniffer.py**: Sniffer de rede em tempo real para análise de pacotes e medição de PPS (Pacotes por Segundo).

3. **DedSec_Infiltration.py**: Automação para auditoria de redes sem fio, capaz de colocar a placa em modo monitor, realizar ataques de desautenticação (Deauth) e capturar *handshakes* para quebra de senha (WPA2/WPS).

## 🛠️ Tecnologias e Dependências
* **Linguagem:** Python 3.12+
* **Bibliotecas:** * `scapy` (Manipulação de pacotes de rede)
    * `colorama` (Interface visual colorida)
* **Requisito Windows:** É necessário instalar o [Npcap](https://npcap.com/) para que o monitor de rede funcione.

## 📦 Como Instalar

1. Clone o repositório:
   ```bash
   git clone 