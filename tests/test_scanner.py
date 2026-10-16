"""Testes da camada de varredura ARP (sem rede real)."""

from __future__ import annotations

from mapeador_rede_lan_arp.scanner import scan_network


def _fake_scan(cidr: str, timeout: float, interface: str | None) -> list[tuple[str, str]]:
    return [
        ("192.168.1.1", "aa:bb:cc:dd:ee:01"),
        ("192.168.1.5", "aa:bb:cc:dd:ee:05"),
        ("192.168.1.50", "aa:bb:cc:dd:ee:32"),
    ]


def test_scan_network_retorna_topologia_com_hosts() -> None:
    topo = scan_network("192.168.1.0/24", arp_scan=_fake_scan)
    assert topo.to_dict()["count"] == 3
    ips = {host.ip for host in topo.hosts}
    assert ips == {"192.168.1.1", "192.168.1.5", "192.168.1.50"}


def test_scan_network_nao_duplica_host_por_ip() -> None:
    def com_duplicado(cidr: str, timeout: float, interface: str | None) -> list[tuple[str, str]]:
        return [
            ("192.168.1.1", "aa:bb:cc:dd:ee:01"),
            ("192.168.1.1", "aa:bb:cc:dd:ee:01"),
        ]

    topo = scan_network("192.168.1.0/24", arp_scan=com_duplicado)
    assert topo.to_dict()["count"] == 1
    assert topo.find_by_ip("192.168.1.1").mac == "aa:bb:cc:dd:ee:01"


def test_scan_network_passa_argumentos_para_scanner() -> None:
    capturado: dict[str, object] = {}

    def espiao(cidr: str, timeout: float, interface: str | None) -> list[tuple[str, str]]:
        capturado["cidr"] = cidr
        capturado["timeout"] = timeout
        capturado["interface"] = interface
        return []

    scan_network("10.0.0.0/8", timeout=5.0, interface="eth0", arp_scan=espiao)
    assert capturado == {"cidr": "10.0.0.0/8", "timeout": 5.0, "interface": "eth0"}


def test_scan_network_vazio_retorna_topologia_vazia() -> None:
    topo = scan_network("192.168.1.0/24", arp_scan=lambda *_: [])
    assert topo.to_dict()["count"] == 0
    assert topo.hosts == []
