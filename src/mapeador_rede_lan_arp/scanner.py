"""Descoberta de hosts LAN via varredura ARP com scapy."""

from __future__ import annotations

from collections.abc import Callable, Iterable

from scapy.all import ARP, Ether, srp  # type: ignore[import-untyped]

from .topology import Host, Topology

ArpScan = Callable[[str, float, str | None], Iterable[tuple[str, str]]]


def _default_arp_scan(
    cidr: str, timeout: float, interface: str | None
) -> list[tuple[str, str]]:
    """Varre a rede com ARP via scapy e retorna lista de (ip, mac).

    Requer privilegios de administrador/root para enviar pacotes brutos.
    """
    pacote = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=cidr)
    respondidos, _nao_respondidos = srp(
        pacote, timeout=timeout, iface=interface, verbose=False
    )
    resultados: list[tuple[str, str]] = []
    for _enviado, recebido in respondidos:
        resultados.append((recebido.psrc, recebido.hwsrc))
    return resultados


def scan_network(
    cidr: str,
    timeout: float = 2.0,
    interface: str | None = None,
    arp_scan: ArpScan | None = None,
) -> Topology:
    """Descobre hosts na rede ``cidr`` via ARP e monta a topologia.

    ``arp_scan`` e um ponto de injecao para testes: recebe (cidr, timeout,
    interface) e deve retornar um iteravel de pares (ip, mac). Por default
    usa a varredura real com scapy.
    """
    scanner = arp_scan or _default_arp_scan
    descobertos = scanner(cidr, timeout, interface)
    topologia = Topology()
    for ip, mac in descobertos:
        topologia.add(Host(ip=ip, mac=mac))
    return topologia
