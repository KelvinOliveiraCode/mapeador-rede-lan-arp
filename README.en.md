# mapeador-rede-lan-arp

**English** · [Português (Brasil)](README.md)

[![Python 3](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](#) [![scapy](https://img.shields.io/badge/scapy-only%20dep-3776AB?style=flat-square)](#) [![pytest](https://img.shields.io/badge/pytest-10%20tests-0A9EDC?style=flat-square&logo=pytest)](#) [![MIT License](https://img.shields.io/badge/License-MIT-f4c430?style=flat-square)](LICENSE)

## What it is

**LAN network mapper via ARP scan**: discovers active hosts on the network by sending ARP packets (via scapy) and builds the MAC/IP topology. It is an educational networking lab focused on layer-2 device discovery.

## Status

An educational lab, working and tested (10 tests).

## Features

- **ARP scan** (`scanner.py`): `scan_network(cidr)` — sends ARP Request packets to every address in the range and collects responses (IP + MAC).
- **Topology** (`topology.py`): `Host` (IP, MAC, timestamp) with IP ordering.
- **Output**: list of discovered hosts with IP, MAC and timestamp.
- **CLI**: `mapeador-rede-lan-arp <CIDR>`.

## Stack

- Python ≥ 3.10
- scapy ≥ 2.5 (only dependency)
- pytest (dev)

## Repository layout

```
mapeador-rede-lan-arp/
├── pyproject.toml · BRIEF.md
├── src/mapeador_rede_lan_arp/
│   ├── scanner.py    # ARP scan via scapy
│   └── topology.py   # Host model
├── tests/            # 10 tests
└── LICENSE           # MIT
```

## Prerequisites and installation

```bash
pip install -e .
```

## How to run

```bash
mapeador-rede-lan-arp 192.168.1.0/24
```
⚠️ Requires admin/root privileges to send raw ARP packets.

## Tests and quality

```bash
PYTHONPATH=src python -m pytest tests/
# 10 passed
```

## Technical decisions and trade-offs

- Scapy for ARP: a mature, straightforward API; the trade-off is a single external dependency.
- Simple CLI: one positional argument (CIDR), no subcommands.

## Known limitations

- ARP scan only reaches hosts on the same broadcast network.
- Requires admin/root for raw packet send/receive.
- Tests use mocks (no real packets sent).

## Development process

An individual project by Kelvin Oliveira, built with orchestrated AI agents and reviewed by the author.

## License and author

MIT — Copyright (c) 2026 Kelvin Rebelo de Oliveira. Author: [Kelvin Oliveira](https://github.com/KelvinOliveiraCode) · [Portfolio](https://kelvinoliveiracode.github.io/portfolio/)
