# WHOIS Client

A simple Python WHOIS client that queries domain information over TCP port 43. This tool helps you look up domain registration details directly from WHOIS servers without relying on external libraries.

## Features

- Performs WHOIS lookups for any domain.
- Automatically selects an appropriate WHOIS server based on the top-level domain (TLD), with a fallback to `whois.iana.org`.
- Lightweight and dependency-free; uses only Python's built-in `socket` module.
- Easy to customize and extend for other TLDs or WHOIS servers.

## Usage

Clone or download the `whois_client.py` script and run it with Python 3. Provide the domain name you want to query as an argument:

```bash
python whois_client.py example.com
```

The script will print the raw WHOIS record to the console. Note that some registrars may limit the number of queries from a single IP address.

## Disclaimer

This project is for educational purposes. Please ensure that you comply with the terms of service of WHOIS providers and respect privacy and legal considerations when performing WHOIS queries.
