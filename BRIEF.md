# BRIEF — mapeador-rede-lan-arp

Projeto: descoberta de hosts LAN via varredura ARP (scapy + Python). Area: Redes.
Dono da validacao: workflow manager (voce).

## Entregas

| Arquivo | Conteudo |
|---|---|
| `pyproject.toml` | Projeto, dependencias (scapy), scripts CLI, grupo dev (pytest, ruff) |
| `src/mapeador_rede_lan_arp/__init__.py` | Pacote, versao 0.1.0 |
| `src/mapeador_rede_lan_arp/topology.py` | Modelos Host e Topology (IP/MAC, sem duplicados por IP, busca, ordenacao) |
| `src/mapeador_rede_lan_arp/scanner.py` | scan_network(cidr, timeout, interface, arp_scan=) — varredura real com scapy, ponto de injeçao para testes |
| `src/mapeador_rede_lan_arp/__main__.py` | CLI: varrede CIDR, saida texto ou JSON (-j) |
| `tests/test_scanner.py` | 4 testes: hosts, sem duplicados, argumentos, rede vazia (scanner falso, sem rede real) |
| `tests/test_topology.py` | 6 testes: campos, validacao, busca IP/MAC, ordenacao deterministica |
| `README.md` | Bilíngue PT-BR + EN: o que faz, como usar, testes, licenca MIT, autor Kelvin Oliveira |
| `BRIEF.md` | Este arquivo |

## Como verificar

No diretorio do projeto:

    uv sync
    uv run ruff check .
    uv run pytest -q

Esperado: ruff sem erros; 10 testes passam (sem necessidade de rede real).

A varredura real (`uv run python -m mapeador_rede_lan_arp 192.168.1.0/24`) requer executar como administrador/root para enviar pacotes brutos.

## Critérios de aceitação (do PLANO_50_PROJETOS.md)

- [x] Topologia gerada (IP + MAC)
- [x] Testes que passem (pytest)
- [x] README PT/EN completo

Licenca: MIT. Autor: Kelvin Oliveira.
