# dns_utilities/dns_tools.py
# ------------------------------------------------------------
# Forward and reverse DNS lookups.
# ------------------------------------------------------------

import socket

def forward_lookup(domain):
    """Resolve domain to IP address."""
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        return f"Error: {e}"


def reverse_lookup(ip):
    """Resolve IP address to hostname."""
    try:
        return socket.gethostbyaddr(ip)
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print("=== DNS Utilities ===")
    choice = input("Forward (F) or Reverse (R) lookup? ").lower()

    if choice == "f":
        domain = input("Enter domain: ")
        print("IP Address:", forward_lookup(domain))
    elif choice == "r":
        ip = input("Enter IP: ")
        print("Hostname:", reverse_lookup(ip))
    else:
        print("Invalid choice.")
