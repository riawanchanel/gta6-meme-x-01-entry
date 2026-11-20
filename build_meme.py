from PIL import Image, ImageDraw, ImageFont

A = "assets"
scene = Image.open(f"{A}/media-generation-meme-scene-skeleton-bench-0-5446274a-6383-4893-809e-017a3c26f644.png").convert("RGB")
W, H = scene.size  # 1600x1600
mark = Image.open(f"{A}/make-fun-press-kit/mark-1024.png").convert("RGBA")
font_path = "/home/hatch/workspace/makefun/gta6-clipper-01-entry/assets/Anton-Regular.ttf"

out = scene.copy()

# ghost as poster inside the store window frame
poster = mark.resize((225, 225), Image.LANCZOS)
out.paste(poster, (155, 225), poster)

# big ghost badge sitting at the right end of the bench
big = mark.resize((470, 470), Image.LANCZOS)
out.paste(big, (1090, 880), big)

# text bands
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
od.rectangle([0, 0, W, 150], fill=(0, 0, 0, 140))
od.rectangle([0, 1400, W, H], fill=(0, 0, 0, 140))
out = Image.alpha_composite(out.convert("RGBA"), overlay)
d = ImageDraw.Draw(out)

def centered(text, y, size):
    f = ImageFont.truetype(font_path, size)
    tw = d.textlength(text, font=f)
    d.text(((W - tw) / 2, y), text, font=f, fill=(255, 255, 255, 255),
           stroke_width=5, stroke_fill=(0, 0, 0, 255))

centered("WAITING FOR GTA 6 SINCE 2013", 28, 92)
centered("MY AI AGENT ALREADY GOT PAID", 1406, 82)
centered("ON MAKE.FUN", 1488, 82)

out.convert("RGB").save("meme.png")
print("saved meme.png", out.size)
