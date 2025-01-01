from pyasic.device.algorithm import MinerAlgo
from pyasic.device.models import MinerModel
from pyasic.miners.device.makes import WhatsMinerMake


class M67SVK30(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M67SVK30

    expected_chips = 440
    expected_fans = 0
    expected_hashboards = 3
    algo = MinerAlgo.SHA256