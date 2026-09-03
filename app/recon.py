from infrastructure.nmap_scanner import run_nmap, parse_scan
from domain.models import Target

def recon(target_ip: str) -> Target:
    xml = run_nmap(target_ip)
    target = parse_scan(xml)

    return target