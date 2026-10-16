# Mapeador de rede LAN via ARP / LAN ARP mapper

Escaneia uma rede local enviando requisicoes ARP e monta a topologia de hosts com endereco IP e MAC. Escrito em Python com scapy.

Scans a local network by sending ARP requests and builds a topology of hosts with IP and MAC addresses. Written in Python with scapy.

## O que faz / What it does

Envia requisicoes ARP para todos os IPs de um bloco CIDR (ex. 192.168.1.0/24), coleta as respostas e devolve a lista de hosts ativos com IP e endereco MAC, ordenada por IP. Sem duplicados.

Sends ARP requests to every IP in a CIDR block (ex. 192.168.1.0/24), collects the replies, and returns the list of active hosts with IP and MAC address, ordered by IP. No duplicates.

## Como usar / How to use

Varredura bruta de pacotes exige administrador (root no Linux, admin no Windows).

Sending raw packets requires administrator (root on Linux, admin on Windows).

Instale as dependencias:

    uv sync

Execute a varredura:

    uv run python -m mapeador_rede_lan_arp 192.168.1.0/24

Run the scan:

    uv run python -m mapeador_rede_lan_arp 192.168.1.0/24

Saida de exemplo:

    Hosts descobertos: 3
      192.168.1.1    aa:bb:cc:dd:ee:01
      192.168.1.5    aa:bb:cc:dd:ee:05
      192.168.1.50   aa:bb:cc:dd:ee:32

Example output:

    Hosts discovered: 3
      192.168.1.1    aa:bb:cc:dd:ee:01
      192.168.1.5    aa:bb:cc:dd:ee:05
      192.168.1.50   aa:bb:cc:dd:ee:32

Saida em JSON:

    uv run python -m mapeador_rede_lan_arp 192.168.1.0/24 -j

JSON output:

    uv run python -m mapeador_rede_lan_arp 192.168.1.0/24 -j

Opcoes:

    -t, --timeout   timeout da varredura em segundos (padrao: 2.0)
    -i, --interface interface de rede (padrao: automatica)
    -j, --json      saida em JSON

Options:

    -t, --timeout   scan timeout in seconds (default: 2.0)
    -i, --interface network interface (default: automatic)
    -j, --json      JSON output

## Testes / Tests

A suíte de teste nao precisa de rede real: a varredura e injetavel com um scanner falso.

    uv run pytest -q

The test suite does not need a real network: the scan is injectable with a fake scanner.

    uv run pytest -q

Todos os testes devem passar.

All tests must pass.

## Licenca / License

MIT.

## Autor / Author

Kelvin Oliveira
