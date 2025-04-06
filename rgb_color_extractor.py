import colorgram

class RgbColorExtractor:
    def __init__(self):
        self.colors_extracted = []

    def extract_rgb_properties(self, image_file, num_colors):
        colors = colorgram.extract(image_file, num_colors)

        for c in range(num_colors):
            color = colors[c]
            rgb = color.rgb
            rgb_set = (rgb[0], rgb[1], rgb[2])
            self.colors_extracted.append(rgb_set)

        return self.colors_extracted
