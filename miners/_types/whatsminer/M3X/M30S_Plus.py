from miners import BaseMiner


class M30SPlus(BaseMiner):
    def __init__(self, ip: str):
        super().__init__()
        self.ip = ip
        self.model = "M30S+"
        self.nominal_chips = 156