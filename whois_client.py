#!/usr/bin/env python3
"""
Simple WHOIS client tool.

This script performs a WHOIS lookup for a given domain by connecting to the WHOIS server on port 43.
It prints the WHOIS record to the console.

Usage:
    python whois_client.py example.com
"""
import sys
import socket


def whois(domain):
    """Perform a WHOIS lookup for the specified domain."""
    # Determine the TLD to choose the appropriate WHOIS server
    tld = domain.split('.')[-1]
    # Mapping of TLDs to WHOIS servers; default to whois.iana.org
    servers = {
        'com': 'whois.verisign-grs.com',
        'net': 'whois.verisign-grs.com',
        'org': 'whois.pir.org',
        'info': 'whois.afilias.net',
        'co': 'whois.nic.co',
        'io': 'whois.nic.io',
    }
    server = servers.get(tld, 'whois.iana.org')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10)
        try:
            s.connect((server, 43))
        except Exception as e:
            print(f"Error connecting to {server}: {e}")
            return None
        query = domain + "\r\n"
        s.send(query.encode())
        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data
    return response.decode(errors='ignore')


def main():
    if len(sys.argv) != 2:
        print("Usage: python whois_client.py <domain>")
        sys.exit(1)
    domain = sys.argv[1]
    result = whois(domain)
    if result:
        print(result)
    else:
        print("Failed to retrieve WHOIS information.")


if __name__ == "__main__":
    main()
