from string import Template
import os


class LabelEnums:
    def __init__(self, labels):
        self.labels = labels
        self.enums = {label: ind for ind, label in enumerate(labels)}

    def construct(self, template):
        a = {}
        for ind, val in self.enums.items():
            if not isinstance(ind, (list, tuple, set, dict)):
                a[ind] = Template(template).substitute(ind=ind, val=val)
            else:
                for i in ind:
                    a[i] = Template(template).substitute(ind=i, val=val)
        return a

    def to_string(self, template):
        return "\n".join(self.construct(template).values())


temp_labels = LabelEnums(
    (
        "TEMP_TILE_SPRITE_OFFSET",
        "TEMP_ON_COAST",
        "TEMP_NEARBY_WATER_STATUS",
        "TEMP_ON_COAST_SHOW_SEA",
        "TEMP_ON_SLANTED_SLOPE",
        "TEMP_GROUND",
        "TEMP_IS_SNOW",
    )
)


class SpritesetEntries:
    entries = tuple(
        Template(e)
        for e in (
            "[0, 0, 64, 31, -31,  0,  \"$path\"]",
            "[0, 0, 64, 31, -31,  0,  \"$path\"]",
            "[0, 0, 64, 23, -31,  0,  \"$path\"]",
            "[0, 0, 64, 23, -31,  0,  \"$path\"]",
            "[0, 0, 64, 31, -31,  0,  \"$path\"]",
            "[0, 0, 64, 31, -31,  0,  \"$path\"]",
            "[0, 0, 64, 23, -31,  0,  \"$path\"]",
            "[0, 0, 64, 23, -31,  0,  \"$path\"]",
            "[0, 0, 64, 39, -31, -8,  \"$path\"]",
            "[0, 0, 64, 39, -31, -8,  \"$path\"]",
            "[0, 0, 64, 31, -31, -8,  \"$path\"]",
            "[0, 0, 64, 31, -31, -8,  \"$path\"]",
            "[0, 0, 64, 39, -31, -8,  \"$path\"]",
            "[0, 0, 64, 39, -31, -8,  \"$path\"]",
            "[0, 0, 64, 31, -31, -8,  \"$path\"]",
            "[0, 0, 64, 47, -31, -16, \"$path\"]",
            "[0, 0, 64, 15, -31,  0,  \"$path\"]",
            "[0, 0, 64, 31, -31, -8,  \"$path\"]",
            "[0, 0, 64, 31, -31, -8,  \"$path\"]",
        )
    )

    def __init__(self, path, max=19):
        self.path = path
        self.max = max
        self.files = {}
        for i in range(self.max):
            if os.path.exists(f"{path}/{i}.png"):
                self.files[i] = f"{path}/{i}.png"

    def construct(self):
        assert (
            len(self.files) <= self.max
        ), f"There should only be {self.max} files at most"
        a = {}
        for i in range(self.max):
            if i in self.files:
                a[i] = self.entries[i].substitute(path=self.files[i])
            else:
                a[i] = "[]"
        return a

    def to_string(self):
        return "\n".join(self.construct().values())


def gen_grounds_spriteset_entries(path):
    return {
        folder: SpritesetEntries(f"{path}/{folder}").to_string()
        for folder in (
            "normal",
            "coastline",
            "normal_2",
            "coastline_2",
            "normal_snow",
            "coastline_snow",
            "normal_2_snow",
            "coastline_2_snow",
        )
    }

if __name__ == "__main__":
    for i in gen_grounds_spriteset_entries("gfx/grounds/gray_bricks").values():
        print(i)
