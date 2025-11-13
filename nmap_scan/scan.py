# nmap_scan/scan.py
# ------------------------------------------------------------
# Simple Nmap-based port scanner using python-nmap.
# ------------------------------------------------------------

import nmap
import argparse


def scan_target(target, ports):
    nm = nmap.PortScanner()
    print(f"Scanning {target} on ports {ports}...")
    nm.scan(target, ports)

    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            for port, details in nm[host][proto].items():
                print(f"  Port {port}: {details['state']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Nmap Port Scanner")
    parser.add_argument("--target", required=True, help="Target IP or domain")
    parser.add_argument("--ports", default="1-1024", help="Port range (default 1-1024)")
    args = parser.parse_args()

    scan_target(args.target, args.ports)
