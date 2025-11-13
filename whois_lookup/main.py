# whois_lookup/main.py
# ------------------------------------------------------------
# Basic WHOIS lookup using socket connections.
# ------------------------------------------------------------

import socket
import sys


def whois_lookup(domain):
    """Perform WHOIS query on a given domain."""
    server = "whois.iana.org"
    port = 43
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.send((domain + "\r\n").encode())

    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data
    s.close()

    print(response.decode(errors="ignore"))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python whois_lookup/main.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    print(f"Performing WHOIS lookup for: {domain}")
    whois_lookup(domain)
