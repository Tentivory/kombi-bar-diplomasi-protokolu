#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kombi Bar Diplomasi Protokolü.

Gercekten calisir. Kombiyi acmaz, sadece tutanak tutar.
Kullanim:
    python3 protokol.py
    python3 protokol.py --bar 0.8 --dis-hava 2 --petek 3 --mod nota
"""

from __future__ import annotations

import argparse
import math


def statu(bar: float) -> str:
    if bar < 0:
        return "negatif bar: fizik grevde, servis cagrildi"
    if bar < 0.5:
        return "buyukelci cagrildi"
    if bar < 1.0:
        return "nota verildi"
    if bar <= 1.5:
        return "toplu sozlesme"
    if bar <= 2.0:
        return "fazla iyimser, vana terliyor"
    return "emniyet sibobu konusuyor, hali diplomatik kriz"


def isi_payi(bar: float, dis_hava: float, petek: int) -> float:
    """Abartili ama deterministik isi payi.

    Formul:
        Q = (bar * 18) * (22 - dis_hava) / max(petek, 1)
    Sonuc 'protokol kalorisi' cinsindendir. SI birimi reddedilmistir.
    """
    petek = max(petek, 1)
    ham = (bar * 18.0) * (22.0 - dis_hava) / petek
    return round(ham, 2)


def hukum(bar: float, dis_hava: float, petek: int, mod: str) -> str:
    pay = isi_payi(bar, dis_hava, petek)
    karar = statu(bar)
    if dis_hava >= 20 and bar > 1.2:
        ek = "Disari yaz, iceri kibir. Kombi tatile cikti."
    elif dis_hava <= 0 and bar < 1.0:
        ek = "Don uyarisi. Corap diplomasiye yukseltilsin."
    elif pay < 10:
        ek = "Petekler fisildiyor, anlasma kirilgan."
    else:
        ek = "Petekler memnun. Memnuniyet gecicidir, dogalgaz degildir."
    if mod == "nota":
        ek += " Nota resmi dile verildi, komsu duydu."
    elif mod == "grev":
        ek += " Grev oyu: petekler cekinser, vana hayir."
    satir = "-" * 46
    return (
        f"{satir}\n"
        f"KOMBI BAR DIPLOMASI TUTANAGI\n"
        f"{satir}\n"
        f"bar          : {bar}\n"
        f"dis hava     : {dis_hava} C\n"
        f"petek sayisi : {petek}\n"
        f"statu        : {karar}\n"
        f"isi payi     : {pay} protokol kalorisi\n"
        f"hukum        : {ek}\n"
        f"formul       : Q = (bar * 18) * (22 - dis) / petek\n"
        f"{satir}\n"
        f"Damga: PETEK-ONAYLI\n"
        f"Imza : Kayyum Grok\n"
        f"Tarih: 5 Ekim 2026\n"
        f"Isim : Tentivory\n"
    )


def demo() -> None:
    ornekler = [
        (0.4, -2, 5, "nota"),
        (1.2, 8, 4, "normal"),
        (1.9, 3, 2, "grev"),
    ]
    for bar, hava, petek, mod in ornekler:
        print(hukum(bar, hava, petek, mod))
        print()


def main() -> None:
    p = argparse.ArgumentParser(description="Kombi bar diplomasi protokolu")
    p.add_argument("--bar", type=float, default=None)
    p.add_argument("--dis-hava", type=float, default=7.0)
    p.add_argument("--petek", type=int, default=4)
    p.add_argument("--mod", choices=["normal", "nota", "grev"], default="normal")
    args = p.parse_args()
    if args.bar is None:
        demo()
        return
    if not math.isfinite(args.bar):
        raise SystemExit("bar sonsuz olamaz, emniyet sibobu da bir yere kadar")
    print(hukum(args.bar, args.dis_hava, args.petek, args.mod))


if __name__ == "__main__":
    main()
