from PIL import Image, ImageEnhance
import re

def enhance_rgb_and_lightness(
    image_path,
    output_path,
    r_factor,
    g_factor,
    b_factor,
    lightness_factor,
    contrast_factor,
):
    if not re.match(r".*\d{1,2}\.png$", image_path):
        print(f"Skipping {image_path} because it doesn't match the pattern")
        return

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

        print(f"Enhancing {file}")

        # example: gfx/grounds/gray_brick_1/coastline/xxx.png
        splitted = file.split("/")
        if splitted[-2].endswith("_snow"):
            continue
        splitted[-2] = splitted[-2] + "_snow"
        output_path = "/".join(splitted)

        enhance_rgb_and_lightness(
            file,
            output_path,
            r_factor=0.7,
            g_factor=0.85,
            b_factor=1.4,
            lightness_factor=1.6,
            contrast_factor=1.12,
        )
