#!/usr/bin/env python3
"""Genere les visuels de promo (posts, stories, image d'apercu) a partir de img/apps/.
Usage : python3 marketing/make_visuels.py   (necessite Pillow)"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "img", "apps")
OUT = os.path.join(ROOT, "marketing", "visuels")
os.makedirs(OUT, exist_ok=True)
BOLD = "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf"
REG = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"

APPS = {
    "voteday": dict(
        titre=["Une question", "par jour.", "A ou B ?"],
        sous="Chaque jour à 17h · vote, compare, garde ta série",
        pied="VoteDay · iPhone · Android bientôt",
        shots=["voteday-01_menu.jpg", "voteday-02_vote.jpg", "voteday-04_ile.jpg"],
        c1=(30, 18, 74), c2=(214, 62, 140), accent=(255, 214, 102)),
    "kotoba": dict(
        titre=["Devine le mot", "en 6 essais."],
        sous="Défi du jour · Aventure · Blitz · Tournoi",
        pied="Kotoba · bientôt sur iPhone et Android",
        shots=["kotoba-01_home.jpg", "kotoba-03_adventure.jpg"],
        c1=(8, 40, 52), c2=(224, 64, 74), accent=(255, 236, 160)),
}

def font(path, size):
    return ImageFont.truetype(path, size)

def gradient(w, h, c1, c2):
    base = Image.new("RGB", (w, h), c1)
    top = Image.new("RGB", (w, h), c2)
    mask = Image.linear_gradient("L").resize((w, h))
    return Image.composite(top, base, mask)

def phone(path, height):
    im = Image.open(os.path.join(IMG, path)).convert("RGB")
    w = int(im.width * height / im.height)
    im = im.resize((w, height), Image.LANCZOS)
    r = int(height * 0.07)
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, height - 1], r, fill=255)
    out = Image.new("RGBA", (w + 16, height + 16), (0, 0, 0, 0))
    ImageDraw.Draw(out).rounded_rectangle([0, 0, w + 15, height + 15], r + 8, fill=(255, 255, 255, 235))
    out.paste(im, (8, 8), mask)
    return out

def paste_rot(canvas, ph, cx, cy, angle):
    shadow = Image.new("RGBA", ph.size, (0, 0, 0, 0))
    shadow.paste((0, 0, 0, 120), mask=ph.split()[3])
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    for layer, off in ((shadow, 14), (ph, 0)):
        rot = layer.rotate(angle, expand=True, resample=Image.BICUBIC)
        canvas.paste(rot, (int(cx - rot.width / 2), int(cy - rot.height / 2) + off), rot)

def centered(d, text, y, f, fill, w):
    bb = d.textbbox((0, 0), text, font=f)
    d.text(((w - (bb[2] - bb[0])) / 2, y), text, font=f, fill=fill)
    return bb[3] - bb[1]

def poster(app, w, h, name):
    a = APPS[app]
    cv = gradient(w, h, a["c1"], a["c2"]).convert("RGBA")
    d = ImageDraw.Draw(cv)
    ft, size = font(BOLD, int(w * 0.095)), int(w * 0.095)
    y = int(h * 0.06)
    for line in a["titre"]:
        hh = centered(d, line, y, ft, (255, 255, 255), w)
        y += int(size * 1.12)
    centered(d, a["sous"], y + 10, font(REG, int(w * 0.036)), a["accent"], w)
    story = h > 1500
    ph_h = int(h * (0.50 if story else 0.46))
    cy = int(h * (0.60 if story else 0.64))
    if len(a["shots"]) == 3:
        side = [(-0.27, -9, 0.86), (0.27, 9, 0.86), (0.0, 0, 1.0)]
    else:
        side = [(-0.2, -6, 1.0), (0.2, 6, 1.0)]
    for i in range(len(a["shots"])):
        dx, ang, sc = side[i]
        ph = phone(a["shots"][i], int(ph_h * sc))
        paste_rot(cv, ph, w / 2 + dx * w, cy + (0 if sc == 1.0 else h * 0.02), ang)
    centered(d, a["pied"], int(h * 0.935), font(BOLD, int(w * 0.034)), (255, 255, 255), w)
    cv.convert("RGB").save(os.path.join(OUT, name), quality=92)

def og(path):
    w, h = 1200, 630
    cv = gradient(w, h, (20, 14, 52), (200, 56, 120)).convert("RGBA")
    d = ImageDraw.Draw(cv)
    d.text((60, 70), "Nos apps", font=font(BOLD, 84), fill=(255, 255, 255))
    d.text((60, 175), "Kotoba · VoteDay", font=font(BOLD, 52), fill=(255, 214, 102))
    d.text((60, 255), "Un jeu de mots en 6 essais.", font=font(REG, 36), fill=(255, 255, 255))
    d.text((60, 305), "Une question par jour, A ou B.", font=font(REG, 36), fill=(255, 255, 255))
    d.text((60, 520), "OKALAM Studio · podcast NPP", font=font(REG, 30), fill=(255, 255, 255))
    for i, (p, x, ang) in enumerate([("kotoba-03_adventure.jpg", 800, 6), ("voteday-02_vote.jpg", 1010, -6)]):
        paste_rot(cv, phone(p, 440), x, 330, ang)
    cv.convert("RGB").save(path, quality=90)

if __name__ == "__main__":
    for app in APPS:
        poster(app, 1080, 1350, f"{app}_post_1080x1350.jpg")
        poster(app, 1080, 1920, f"{app}_story_1080x1920.jpg")
    og(os.path.join(IMG, "apps-og.jpg"))
    print("ok")
