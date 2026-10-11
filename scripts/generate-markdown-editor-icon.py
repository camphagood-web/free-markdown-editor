from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "packages" / "desktop" / "static"


def build_icon() -> Image.Image:
    size = 1024
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    draw.rounded_rectangle((74, 74, 950, 950), radius=205, fill=(38, 106, 168, 255))
    draw.rounded_rectangle((105, 105, 919, 919), radius=174, outline=(130, 190, 235, 110), width=10)

    # A white document and folded corner read clearly at Dock icon sizes.
    draw.rounded_rectangle((273, 202, 751, 820), radius=42, fill=(255, 255, 255, 255))
    draw.polygon(((613, 202), (751, 340), (613, 340)), fill=(207, 229, 246, 255))
    draw.line(((613, 202), (613, 340), (751, 340)), fill=(114, 165, 205, 255), width=9)

    ink = (38, 106, 168, 255)
    draw.line(((340, 565), (340, 447), (386, 504), (432, 447), (432, 565)), fill=ink, width=28, joint="curve")
    draw.line(((514, 447), (514, 547)), fill=ink, width=28)
    draw.polygon(((466, 524), (562, 524), (514, 582)), fill=ink)
    draw.rounded_rectangle((336, 625, 687, 644), radius=9, fill=(202, 221, 235, 255))
    draw.rounded_rectangle((336, 670, 607, 689), radius=9, fill=(202, 221, 235, 255))
    return image


def main() -> None:
    image = build_icon()
    image.save(STATIC / "icon.png")
    image.resize((256, 256), Image.Resampling.LANCZOS).save(
        ROOT / "packages" / "desktop" / "src" / "renderer" / "src" / "assets" / "images" / "logo.png"
    )

    image.save(STATIC / "icon.icns", format="ICNS")


if __name__ == "__main__":
    main()
