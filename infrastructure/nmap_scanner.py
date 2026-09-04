import subprocess
import xml.etree.ElementTree as ET
from domain.models import Service, Port, Target

def parse_scan(xml_text: str) -> Target:
    root = ET.fromstring(xml_text)
    host = root.find("host")
    ip = host.find("address").get("addr")
    ports = []
    for port_elem in host.findall("ports/port"):
        state = port_elem.find("state").get("state")
        service_elem = port_elem.find("service")
        service = Service(
            name=service_elem.get("name"),
            version=service_elem.get("version"),
            product=service_elem.get("product"),
        )
        port = Port(
            number=int(port_elem.get("portid")),
            protocol=port_elem.get("protocol"),
            state=state,
            service=service,
        )
        ports.append(port)

    return Target(ip=ip, ports=ports)

def run_nmap(ip: str) -> str:
	result = subprocess.run(
		["nmap", "-oX", "-", "-sV", ip],
		capture_output=True,
		text=True,
	)
     
	return result.stdout
