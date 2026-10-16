"""Testes do modelo de topologia."""

from __future__ import annotations

from mapeador_rede_lan_arp.topology import Host, Topology


def test_host_armazena_ip_e_mac() -> None:
    host = Host(ip="192.168.1.1", mac="aa:bb:cc:dd:ee:01")
    assert host.ip == "192.168.1.1"
    assert host.mac == "aa:bb:cc:dd:ee:01"


def test_host_rejeita_campos_vazios() -> None:
    try:
        Host(ip="", mac="aa:bb:cc:dd:ee:01")
    except ValueError:
        pass
    else:  # pragma: no cover - assert executado se nao houver excecao
        raise AssertionError("ip vazio deveria lancar ValueError")
    try:
        Host(ip="192.168.1.1", mac="")
    except ValueError:
        pass
    else:  # pragma: no cover
        raise AssertionError("mac vazio deveria lancar ValueError")


def test_topology_adiciona_host() -> None:
    topo = Topology()
    topo.add(Host(ip="192.168.1.1", mac="aa:bb:cc:dd:ee:01"))
    assert topo.to_dict()["count"] == 1


def test_topology_nao_duplica_por_ip() -> None:
    topo = Topology()
    topo.add(Host(ip="192.168.1.1", mac="aa:bb:cc:dd:ee:01"))
    topo.add(Host(ip="192.168.1.1", mac="ff:ff:ff:ff:ff:ff"))
    assert topo.to_dict()["count"] == 1
    assert topo.find_by_ip("192.168.1.1").mac == "aa:bb:cc:dd:ee:01"


def test_topology_find_by_mac() -> None:
    topo = Topology()
    topo.add(Host(ip="192.168.1.1", mac="aa:bb:cc:dd:ee:01"))
    assert topo.find_by_mac("aa:bb:cc:dd:ee:01") is not None
    assert topo.find_by_mac("00:00:00:00:00:00") is None


def test_topology_sorted_by_ip_eh_deterministico() -> None:
    topo = Topology()
    topo.add(Host(ip="192.168.1.50", mac="aa:bb:cc:dd:ee:32"))
    topo.add(Host(ip="192.168.1.2", mac="aa:bb:cc:dd:ee:02"))
    ips = [host.ip for host in topo.sorted_by_ip()]
    assert ips == ["192.168.1.2", "192.168.1.50"]
