import ipaddress
from urllib.parse import urlparse

def is_private_url(url):
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname
        if not hostname:
            return False
        ip = ipaddress.ip_address(hostname)
        return ip.is_private
    except ValueError:
        return False