from dataclasses import dataclass, field

@dataclass
class Service:
	name: str | None = None
	version: str | None = None
	product: str | None = None


@dataclass
class Port:
	service: Service
	protocol: str
	number: int
	state: str


@dataclass
class Target:
	ip: str
	ports: list[Port] = field(default_factory=list)