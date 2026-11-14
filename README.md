# mapeador-rede-lan-arp

[English](README.en.md) · **Português (Brasil)**

[![Python 3](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](#) [![scapy](https://img.shields.io/badge/scapy-%C3%BAnica%20dep-3776AB?style=flat-square)](#) [![pytest](https://img.shields.io/badge/pytest-10%20testes-0A9EDC?style=flat-square&logo=pytest)](#) [![MIT License](https://img.shields.io/badge/License-MIT-f4c430?style=flat-square)](LICENSE)

## O que é

**Mapeador de rede LAN via varredura ARP**: descobre hosts ativos na rede enviando pacotes ARP (via scapy) e monta a topologia MAC/IP. É um laboratório educacional de redes com foco em descoberta de dispositivos na camada 2.

## Status

Laboratório educacional funcional e testado (10 testes).

## Funcionalidades

- **Varredura ARP** (`scanner.py`): `scan_network(cidr)` — envia pacotes ARP Request para todos os endereços da faixa e coleta as respostas (IP + MAC).
- **Topologia** (`topology.py`): `Host` (IP, MAC, timestamp) com ordenação por IP.
- **Saída**: lista de hosts descobertos com IP, MAC e instante.
- **CLI**: `mapeador-rede-lan-arp <CIDR>`.

## Stack

- Python ≥ 3.10
- scapy ≥ 2.5 (única dependência)
- pytest (dev)

## Estrutura do repositório

```
mapeador-rede-lan-arp/
├── pyproject.toml · BRIEF.md
├── src/mapeador_rede_lan_arp/
│   ├── scanner.py    # varredura ARP com scapy
│   └── topology.py   # modelo Host
├── tests/            # 10 testes
└── LICENSE           # MIT
```

## Pré-requisitos e instalação

```bash
pip install -e .
```

## Como executar

```bash
mapeador-rede-lan-arp 192.168.1.0/24
```
⚠️ Requer privilégios de administrador/root para enviar pacotes ARP.

## Testes e qualidade

```bash
PYTHONPATH=src python -m pytest tests/
# 10 passed
```

## Decisões técnicas e trade-offs

- Scapy para ARP: API madura e direta; em troca, é a única dependência externa.
- CLI simples: um argumento posicional (CIDR), sem subcomandos.

## Limitações conhecidas

- A varredura ARP só alcança hosts na mesma rede broadcast.
- Requer privilégios de admin/root para enviar/receber pacotes raw.
- Os testes usam mock (não enviam pacotes reais).

## Processo de desenvolvimento

Projeto individual de Kelvin Oliveira, construído com agentes de IA orquestrados e revisado pelo autor.

## Licença e autor

MIT — Copyright (c) 2026 Kelvin Rebelo de Oliveira. Autor: [Kelvin Oliveira](https://github.com/KelvinOliveiraCode) · [Portfólio](https://kelvinoliveiracode.github.io/portfolio/)
