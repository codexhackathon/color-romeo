#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

import svgwrite
import colorbrewer

from character_colors import character_colors


def load_json_data():
    return json.load(open('./romeo_analysis_array.json', 'r'))

def process_data():
    romeo_array = load_json_data()
    drawing = svgwrite.Drawing('08_romeo_colors.svg', size=(500,5000), profile='tiny')
    offset = 0
    def y_position(count, offset):
        return count + offset
    for count, line in enumerate(romeo_array):
        svg_line = drawing.add(drawing.line(
            (0, y_position(count, offset)),
            (100, y_position(count, offset)),
            stroke=character_colors[line['speaker']],
        ))

    drawing.save()

if __name__ == "__main__":
    process_data()
