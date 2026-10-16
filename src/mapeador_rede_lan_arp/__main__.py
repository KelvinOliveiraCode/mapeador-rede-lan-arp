"""CLI do mapeador de rede LAN via varredura ARP."""

from __future__ import annotations

import argparse
import json
import sys

from .scanner import scan_network


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mapeador-rede-lan-arp",
        description=(
            "Descobre hosts na LAN via varredura ARP e monta a topologia MAC/IP."
        ),
    )
    parser.add_argument(
        "cidr",
        help="Rede a varrer, ex. 192.168.1.0/24",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=2.0,
        help="Timeout da varredura em segundos (default: 2.0)",
    )
    parser.add_argument(
        "-i",
        "--interface",
        default=None,
        help="Interface de rede (default: automatica)",
    )
    parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        help="Saida em JSON",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        topologia = scan_network(
            cidr=args.cidr, timeout=args.timeout, interface=args.interface
        )
    except PermissionError as exc:
        print(
            f"erro: necessario executar como administrador/root para enviar pacotes ARP: {exc}",
            file=sys.stderr,
        )
        return 1
    except Exception as exc:  # noqa: BLE001 - fronteira de CLI reporta ao usuario
        print(f"erro: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(topologia.to_dict(), ensure_ascii=False, indent=2))
    else:
        hosts = topologia.sorted_by_ip()
        print(f"Hosts descobertos: {len(hosts)}")
        for host in hosts:
            print(f"  {host.ip:<16} {host.mac}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
