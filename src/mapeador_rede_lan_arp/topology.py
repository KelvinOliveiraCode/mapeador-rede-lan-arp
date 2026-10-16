"""Modelo de dados da topologia LAN descoberta via ARP."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class Host:
    """Um host da LAN: endereco IP, endereco MAC e instante da descoberta."""

    ip: str
    mac: str
    discovered_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def __post_init__(self) -> None:
        if not self.ip:
            raise ValueError("ip nao pode estar vazio")
        if not self.mac:
            raise ValueError("mac nao pode estar vazio")


@dataclass
class Topology:
    """Topologia da rede: conjunto de hosts descobertos, sem duplicar por IP."""

    hosts: list[Host] = field(default_factory=list)

    def add(self, host: Host) -> None:
        """Adiciona um host sem duplicar um ja cadastrado pelo mesmo IP."""
        for existente in self.hosts:
            if existente.ip == host.ip:
                return
        self.hosts.append(host)

    def find_by_ip(self, ip: str) -> Host | None:
        """Retorna o host com o IP informado, ou None se nao houver."""
        for host in self.hosts:
            if host.ip == ip:
                return host
        return None

    def find_by_mac(self, mac: str) -> Host | None:
        """Retorna o host com o MAC informado, ou None se nao houver."""
        for host in self.hosts:
            if host.mac == mac:
                return host
        return None

    def sorted_by_ip(self) -> list[Host]:
        """Retorna os hosts ordenados por endereco IP (deterministico)."""
        return sorted(self.hosts, key=lambda host: host.ip)

    def to_dict(self) -> dict[str, object]:
        """Serializa a topologia para dicionario (JSON-serializavel)."""
        return {
            "hosts": [
                {
                    "ip": host.ip,
                    "mac": host.mac,
                    "discovered_at": host.discovered_at,
                }
                for host in self.sorted_by_ip()
            ],
            "count": len(self.hosts),
        }
