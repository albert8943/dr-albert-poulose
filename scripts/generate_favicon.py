"""Generate Google-friendly favicons from static/images/profile.jpg."""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "static" / "images" / "profile.jpg"
OUT = ROOT / "static"


def main() -> None:
    img = Image.open(SRC).convert("RGB")
    w, h = img.size
    print(f"source: {w}x{h}")

    # Tight upper-center crop so the face reads at 16–48px.
    side = min(w, h)
    crop_side = int(side * 0.55)
    cx = w // 2
    cy = int(h * 0.32)
    left = max(0, min(cx - crop_side // 2, w - crop_side))
    top = max(0, min(cy - crop_side // 2, h - crop_side))
    face = img.crop((left, top, left + crop_side, top + crop_side))
    print(f"face crop: {crop_side}x{crop_side} @ ({left},{top})")

    sizes = {
        "favicon-32x32.png": 32,
        "favicon-48x48.png": 48,
        "apple-touch-icon.png": 180,
        "android-chrome-192x192.png": 192,
    }
    for name, size in sizes.items():
        path = OUT / name
        face.resize((size, size), Image.Resampling.LANCZOS).save(
            path, format="PNG", optimize=True
        )
        print(f"wrote {path.name} ({path.stat().st_size} bytes)")

    ico_sizes = [(16, 16), (32, 32), (48, 48)]
    ico_images = [face.resize(s, Image.Resampling.LANCZOS) for s in ico_sizes]
    ico_path = OUT / "favicon.ico"
    ico_images[0].save(
        ico_path, format="ICO", sizes=ico_sizes, append_images=ico_images[1:]
    )
    print(f"wrote {ico_path.name} ({ico_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
