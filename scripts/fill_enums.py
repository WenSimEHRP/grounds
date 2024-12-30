import sys
from string import Template
import enums


def read_template(path):
    try:
        with open(path, "r") as f:
            return Template(f.read())
    except Exception as e:
        print(f"Error reading template file: {e}")
        sys.exit(1)


def fill_enums(template_path, output_path, labels: dict):
    template = read_template(template_path)
    filled = template.substitute(**labels)
    try:
        with open(output_path, "w+") as f:
            f.write(filled)
    except Exception as e:
        print(f"Error writing to output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    fill_enums(
        "src/objects.pynml",
        "src/objects.gnml", # generated... nml?
        {"temp_enums": enums.temp_labels.to_string("const $ind = $val;")},
    )
    fill_enums(
        "src/items.pynml",
        "src/items.gnml",
        {
            "name": "gray_brick_1",
            **enums.gen_grounds_spriteset_entries("gfx/grounds/gray_brick_1")
        },
    )