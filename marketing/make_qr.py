#!/usr/bin/env python3
"""Génère un QR code SVG local vers la page /apps/ (outil de dev, pas de dépendance runtime).

Usage : pip install segno && python3 marketing/make_qr.py https://TON-DOMAINE/apps/
"""
import sys
import segno

if len(sys.argv) != 2 or not sys.argv[1].startswith("https://"):
    sys.exit("Usage : make_qr.py https://TON-DOMAINE/apps/")
qr = segno.make(sys.argv[1], error="m")
qr.save("marketing/qr/qr-apps.svg", scale=10, border=4, dark="#000000", light="#ffffff",
        title="QR code vers la page des apps OKALAM Studio")
qr.save("marketing/qr/qr-apps.png", scale=12, border=4)
print("OK :", sys.argv[1])
