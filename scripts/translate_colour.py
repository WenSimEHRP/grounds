from PIL import Image, ImageEnhance


def enhance_rgb_and_lightness(
    image_path,
    output_path,
    r_factor,
    g_factor,
    b_factor,
    lightness_factor,
    contrast_factor,
):
    image = Image.open(image_path)

    if image.mode == "RGBA":
        r, g, b, a = image.split()
    else:
        print(f"Image {image_path} is not RGBA")
        return

    r = ImageEnhance.Brightness(r).enhance(r_factor)
    g = ImageEnhance.Brightness(g).enhance(g_factor)
    b = ImageEnhance.Brightness(b).enhance(b_factor)

    image_enhanced = Image.merge("RGBA", (r, g, b, a))
    image_enhanced = ImageEnhance.Contrast(image_enhanced).enhance(contrast_factor)
    image_enhanced = ImageEnhance.Brightness(image_enhanced).enhance(lightness_factor)
    image_enhanced.save(output_path)


if __name__ == "__main__":
    import glob

    for file in glob.glob("gfx/grounds/gray_brick_1/**/*.png", recursive=True):
        if file.endswith("_enhanced.png"):
            continue

        enhance_rgb_and_lightness(
            file,
            file.replace(".png", "_enhanced.png"),
            r_factor=0.7,
            g_factor=0.85,
            b_factor=1.4,
            lightness_factor=1.6,
            contrast_factor=1.12,
        )
