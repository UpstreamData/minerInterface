from enum import Enum


class MinerModelType(str, Enum):
    pass


class AntminerModels(MinerModelType):
    D3 = "D3"
    HS3 = "HS3"
    L3Plus = "L3+"
    KA3 = "KA3"
    KS3 = "KS3"
    DR5 = "DR5"
    KS5 = "KS5"
    L7 = "L7"
    K7 = "K7"
    D7 = "D7"
    E9Pro = "E9Pro"
    S9 = "S9"
    S9i = "S9i"
    S9j = "S9j"
    T9 = "T9"
    D9 = "D9"
    L9 = "L9"
    Z15 = "Z15"
    Z15Pro = "Z15 Pro"
    S17 = "S17"
    S17Plus = "S17+"
    S17Pro = "S17 Pro"
    S17e = "S17e"
    T17 = "T17"
    T17Plus = "T17+"
    T17e = "T17e"
    S19 = "S19"
    S19NoPIC = "S19 No PIC"
    S19L = "S19L"
    S19Pro = "S19 Pro"
    S19j = "S19j"
    S19i = "S19i"
    S19Plus = "S19+"
    S19jNoPIC = "S19j No PIC"
    S19ProPlus = "S19 Pro+"
    S19jPro = "S19j Pro"
    S19jProNoPIC = "S19j Pro No PIC"
    S19jProPlus = "S19j Pro+"
    S19jProPlusNoPIC = "S19j Pro+ No PIC"
    S19XP = "S19 XP"
    S19a = "S19a"
    S19aPro = "S19a Pro"
    S19Hydro = "S19 Hydro"
    S19ProHydro = "S19 Pro Hydro"
    S19ProPlusHydro = "S19 Pro+ Hydro"
    S19KPro = "S19K Pro"
    S19kPro = "S19k Pro"
    S19kProNoPIC = "S19k Pro No PIC"
    T19 = "T19"
    S21 = "S21"
    S21Pro = "S21 Pro"
    T21 = "T21"

    def __str__(self):
        return self.value


class WhatsminerModels(MinerModelType):
    M20V10 = "M20 V10"
    M20SV10 = "M20S V10"
    M20SV20 = "M20S V20"
    M20SV30 = "M20S V30"
    M20PV10 = "M20P V10"
    M20PV30 = "M20P V30"
    M20SPlusV30 = "M20S+ V30"
    M21V10 = "M21 V10"
    M21SV20 = "M21S V20"
    M21SV60 = "M21S V60"
    M21SV70 = "M21S V70"
    M21SPlusV20 = "M21S+ V20"
    M29V10 = "M29 V10"
    M30V10 = "M30 V10"
    M30V20 = "M30 V20"
    M30KV10 = "M30K V10"
    M30LV10 = "M30L V10"
    M30SV10 = "M30S V10"
    M30SV20 = "M30S V20"
    M30SV30 = "M30S V30"
    M30SV40 = "M30S V40"
    M30SV50 = "M30S V50"
    M30SV60 = "M30S V60"
    M30SV70 = "M30S V70"
    M30SV80 = "M30S V80"
    M30SVE10 = "M30S VE10"
    M30SVE20 = "M30S VE20"
    M30SVE30 = "M30S VE30"
    M30SVE40 = "M30S VE40"
    M30SVE50 = "M30S VE50"
    M30SVE60 = "M30S VE60"
    M30SVE70 = "M30S VE70"
    M30SVF10 = "M30S VF10"
    M30SVF20 = "M30S VF20"
    M30SVF30 = "M30S VF30"
    M30SVG10 = "M30S VG10"
    M30SVG20 = "M30S VG20"
    M30SVG30 = "M30S VG30"
    M30SVG40 = "M30S VG40"
    M30SVH10 = "M30S VH10"
    M30SVH20 = "M30S VH20"
    M30SVH30 = "M30S VH30"
    M30SVH40 = "M30S VH40"
    M30SVH50 = "M30S VH50"
    M30SVH60 = "M30S VH60"
    M30SVI20 = "M30S VI20"
    M30SPlusV10 = "M30S+ V10"
    M30SPlusV20 = "M30S+ V20"
    M30SPlusV30 = "M30S+ V30"
    M30SPlusV40 = "M30S+ V40"
    M30SPlusV50 = "M30S+ V50"
    M30SPlusV60 = "M30S+ V60"
    M30SPlusV70 = "M30S+ V70"
    M30SPlusV80 = "M30S+ V80"
    M30SPlusV90 = "M30S+ V90"
    M30SPlusV100 = "M30S+ V100"
    M30SPlusVE30 = "M30S+ VE30"
    M30SPlusVE40 = "M30S+ VE40"
    M30SPlusVE50 = "M30S+ VE50"
    M30SPlusVE60 = "M30S+ VE60"
    M30SPlusVE70 = "M30S+ VE70"
    M30SPlusVE80 = "M30S+ VE80"
    M30SPlusVE90 = "M30S+ VE90"
    M30SPlusVE100 = "M30S+ VE100"
    M30SPlusVF20 = "M30S+ VF20"
    M30SPlusVF30 = "M30S+ VF30"
    M30SPlusVG20 = "M30S+ VG20"
    M30SPlusVG30 = "M30S+ VG30"
    M30SPlusVG40 = "M30S+ VG40"
    M30SPlusVG50 = "M30S+ VG50"
    M30SPlusVG60 = "M30S+ VG60"
    M30SPlusVH10 = "M30S+ VH10"
    M30SPlusVH20 = "M30S+ VH20"
    M30SPlusVH30 = "M30S+ VH30"
    M30SPlusVH40 = "M30S+ VH40"
    M30SPlusVH50 = "M30S+ VH50"
    M30SPlusVH60 = "M30S+ VH60"
    M30SPlusPlusV10 = "M30S++ V10"
    M30SPlusPlusV20 = "M30S++ V20"
    M30SPlusPlusVE30 = "M30S++ VE30"
    M30SPlusPlusVE40 = "M30S++ VE40"
    M30SPlusPlusVE50 = "M30S++ VE50"
    M30SPlusPlusVF40 = "M30S++ VF40"
    M30SPlusPlusVG30 = "M30S++ VG30"
    M30SPlusPlusVG40 = "M30S++ VG40"
    M30SPlusPlusVG50 = "M30S++ VG50"
    M30SPlusPlusVH10 = "M30S++ VH10"
    M30SPlusPlusVH20 = "M30S++ VH20"
    M30SPlusPlusVH30 = "M30S++ VH30"
    M30SPlusPlusVH40 = "M30S++ VH40"
    M30SPlusPlusVH50 = "M30S++ VH50"
    M30SPlusPlusVH60 = "M30S++ VH60"
    M30SPlusPlusVH70 = "M30S++ VH70"
    M30SPlusPlusVH80 = "M30S++ VH80"
    M30SPlusPlusVH90 = "M30S++ VH90"
    M30SPlusPlusVH100 = "M30S++ VH100"
    M30SPlusPlusVJ20 = "M30S++ VJ20"
    M30SPlusPlusVJ30 = "M30S++ VJ30"
    M31V10 = "M31 V10"
    M31V20 = "M31 V20"
    M31HV10 = "M31H V10"
    M31HV40 = "M31H V40"
    M31LV10 = "M30L V10"
    M31SV10 = "M31S V10"
    M31SV20 = "M31S V20"
    M31SV30 = "M31S V30"
    M31SV40 = "M31S V40"
    M31SV50 = "M31S V50"
    M31SV60 = "M31S V60"
    M31SV70 = "M31S V70"
    M31SV80 = "M31S V80"
    M31SV90 = "M31S V90"
    M31SVE10 = "M31S VE10"
    M31SVE20 = "M31S VE20"
    M31SVE30 = "M31S VE30"
    M31SEV10 = "M31SE V10"
    M31SEV20 = "M31SE V20"
    M31SEV30 = "M31SE V30"
    M31SPlusV10 = "M31S+ V10"
    M31SPlusV20 = "M31S+ V20"
    M31SPlusV30 = "M31S+ V30"
    M31SPlusV40 = "M31S+ V40"
    M31SPlusV50 = "M31S+ V50"
    M31SPlusV60 = "M31S+ V60"
    M31SPlusV80 = "M31S+ V80"
    M31SPlusV90 = "M31S+ V90"
    M31SPlusV100 = "M31S+ V100"
    M31SPlusVE10 = "M31S+ VE10"
    M31SPlusVE20 = "M31S+ VE20"
    M31SPlusVE30 = "M31S+ VE30"
    M31SPlusVE40 = "M31S+ VE40"
    M31SPlusVE50 = "M31S+ VE50"
    M31SPlusVE60 = "M31S+ VE60"
    M31SPlusVE80 = "M31S+ VE80"
    M31SPlusVF20 = "M31S+ VF20"
    M31SPlusVF30 = "M31S+ VF30"
    M31SPlusVG20 = "M31S+ VG20"
    M31SPlusVG30 = "M31S+ VG30"
    M32V10 = "M32 V10"
    M32V20 = "M32 V20"
    M32S = "M32S"
    M33V10 = "M33 V10"
    M33V20 = "M33 V20"
    M33V30 = "M33 V30"
    M33SVG30 = "M33S VG30"
    M33SPlusVG20 = "M33S+ VG20"
    M33SPlusVH20 = "M33S+ VH20"
    M33SPlusVH30 = "M33S+ VH30"
    M33SPlusPlusVH20 = "M33S++ VH20"
    M33SPlusPlusVH30 = "M33S++ VH30"
    M33SPlusPlusVG40 = "M33S++ VG40"
    M34SPlusVE10 = "M34S+ VE10"
    M36SVE10 = "M36S VE10"
    M36SPlusVG30 = "M36S+ VG30"
    M36SPlusPlusVH30 = "M36S++ VH30"
    M39V10 = "M39 V10"
    M39V20 = "M39 V20"
    M39V30 = "M39 V30"
    M50VE30 = "M50 VE30"
    M50VG30 = "M50 VG30"
    M50VH10 = "M50 VH10"
    M50VH20 = "M50 VH20"
    M50VH30 = "M50 VH30"
    M50VH40 = "M50 VH40"
    M50VH50 = "M50 VH50"
    M50VH60 = "M50 VH60"
    M50VH70 = "M50 VH70"
    M50VH80 = "M50 VH80"
    M50VH90 = "M50 VH90"
    M50VJ10 = "M50 VJ10"
    M50VJ20 = "M50 VJ20"
    M50VJ30 = "M50 VJ30"
    M50SVJ10 = "M50S VJ10"
    M50SVJ20 = "M50S VJ20"
    M50SVJ30 = "M50S VJ30"
    M50SVH10 = "M50S VH10"
    M50SVH20 = "M50S VH20"
    M50SVH30 = "M50S VH30"
    M50SVH40 = "M50S VH40"
    M50SVH50 = "M50S VH50"
    M50SPlusVH30 = "M50S+ VH30"
    M50SPlusVH40 = "M50S+ VH40"
    M50SPlusVJ30 = "M50S+ VJ30"
    M50SPlusVK20 = "M50S+ VK20"
    M50SPlusPlusVK10 = "M50S++ VK10"
    M50SPlusPlusVK20 = "M50S++ VK20"
    M50SPlusPlusVK30 = "M50S++ VK30"
    M53VH30 = "M53 VH30"
    M53SVH30 = "M53S VH30"
    M53SVJ40 = "M53S VJ40"
    M53SPlusVJ30 = "M53S+ VJ30"
    M53SPlusPlusVK10 = "M53S++ VK10"
    M56VH30 = "M56 VH30"
    M56SVH30 = "M56S VH30"
    M56SPlusVJ30 = "M56S+ VJ30"
    M59VH30 = "M59 VH30"
    M60VK10 = "M60 VK10"
    M60VK20 = "M60 VK20"
    M60VK30 = "M60 VK30"
    M60VK40 = "M60 VK40"
    M60SVK10 = "M60S VK10"
    M60SVK20 = "M60S VK20"
    M60SVK30 = "M60S VK30"
    M60SVK40 = "M60S VK40"
    M63VK10 = "M63 VK10"
    M63VK20 = "M63 VK20"
    M63VK30 = "M63 VK30"
    M63SVK10 = "M63S VK10"
    M63SVK20 = "M63S VK20"
    M63SVK30 = "M63S VK30"
    M66VK20 = "M66 VK20"
    M66VK30 = "M66 VK30"
    M66SVK20 = "M66S VK20"
    M66SVK30 = "M66S VK30"
    M66SVK40 = "M66S VK40"

    def __str__(self):
        return self.value


class AvalonminerModels(MinerModelType):
    Avalon721 = "Avalon 721"
    Avalon741 = "Avalon 741"
    Avalon761 = "Avalon 761"
    Avalon821 = "Avalon 821"
    Avalon841 = "Avalon 841"
    Avalon851 = "Avalon 851"
    Avalon921 = "Avalon 921"
    Avalon1026 = "Avalon 1026"
    Avalon1047 = "Avalon 1047"
    Avalon1066 = "Avalon 1066"
    Avalon1166Pro = "Avalon 1166 Pro"
    Avalon1126Pro = "Avalon 1126 Pro"
    Avalon1246 = "Avalon 1246"
    AvalonNano3 = "Avalon Nano 3"

    def __str__(self):
        return self.value


class InnosiliconModels(MinerModelType):
    T3HPlus = "T3H+"
    A10X = "A10X"
    A11 = "A11"
    A11MX = "A11MX"

    def __str__(self):
        return self.value


class GoldshellModels(MinerModelType):
    CK5 = "CK5"
    HS5 = "HS5"
    KD5 = "KD5"
    KDMax = "KD Max"
    KDBoxII = "KD Box II"
    KDBoxPro = "KD Box Pro"

    def __str__(self):
        return self.value


class ePICModels(MinerModelType):
    BM520i = "BlockMiner 520i"
    BM720i = "BlockMiner 720i"

    def __str__(self):
        return self.value


class AuradineModels(MinerModelType):
    AT1500 = "AT1500"
    AT2860 = "AT2860"
    AT2880 = "AT2880"
    AI2500 = "AI2500"
    AI3680 = "AI3680"
    AD2500 = "AD2500"
    AD3500 = "AD3500"

    def __str__(self):
        return self.value


class BitAxeModels(MinerModelType):
    BM1366 = "Ultra"
    BM1368 = "Supra"
    BM1397 = "Max"
    BM1370 = "Gamma"

    def __str__(self):
        return self.value


class IceRiverModels(MinerModelType):
    KS0 = "KS0"
    KS1 = "KS1"
    KS2 = "KS2"
    KS3 = "KS3"
    KS3L = "KS3L"
    KS3M = "KS3M"
    KS5 = "KS5"
    KS5L = "KS5L"
    KS5M = "KS5M"

    def __str__(self):
        return self.value


class HammerModels(MinerModelType):
    D10 = "D10"

    def __str__(self):
        return self.value


class BraiinsModels(MinerModelType):
    BMM100 = "BMM100"
    BMM101 = "BMM101"


class MinerModel:
    ANTMINER = AntminerModels
    WHATSMINER = WhatsminerModels
    AVALONMINER = AvalonminerModels
    INNOSILICON = InnosiliconModels
    GOLDSHELL = GoldshellModels
    AURADINE = AuradineModels
    EPIC = ePICModels
    BITAXE = BitAxeModels
    ICERIVER = IceRiverModels
    HAMMER = HammerModels
    BRAIINS = BraiinsModels
