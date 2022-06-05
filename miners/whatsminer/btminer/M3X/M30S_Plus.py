from miners._backends import BTMiner  # noqa - Ignore access to _module
from miners._types import M30SPlus, M30SPlusVE40  # noqa - Ignore access to _module


class BTMinerM30SPlus(BTMiner, M30SPlus):
    def __init__(self, ip: str) -> None:
        super().__init__(ip)
        self.ip = ip


class BTMinerM30SPlusVE40(BTMiner, M30SPlusVE40):
    def __init__(self, ip: str) -> None:
        super().__init__(ip)
        self.ip = ip
