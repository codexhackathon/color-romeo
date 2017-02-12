#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

import svgwrite
import colorbrewer

from character_colors import character_colors


def load_json_data():
    return json.load(open('./romeo_analysis_array.json', 'r'))

def y_position(count, offset):
    return count + offset


def process_data():
    romeo_array = load_json_data()
    drawing = svgwrite.Drawing('09_romeo_colors.svg', size=(550,5000), profile='tiny')
    x_offset = 0
    y_offset = 0
    act = ''
    scene = ''
    for count, line in enumerate(romeo_array):
        if line['act'] != act:
            act = line['act']
            act_group = drawing.add(drawing.g(id=act.replace(' ', '-')))
            y_offset += 5
            act_group.add(drawing.line(
                (0, y_position(count, y_offset)),
                (100, y_position(count, y_offset)),
                stroke='red'
            ))
            act_group.translate(x_offset, -y_position(count, y_offset)
            x_offset += 100


        if line['scene'] != scene:
            y_offset += 3
            act_group.add(drawing.line(
                (5, y_position(count, y_offset)),
                (95, y_position(count, y_offset)),
                stroke='blue'
            ))
            scene = line['scene']


        svg_line = act_group.add(drawing.line(
            (10, y_position(count, y_offset)),
            (90, y_position(count, y_offset)),
            stroke=character_colors[line['speaker']],
        ))

    drawing.save()

if __name__ == "__main__":
    process_data()
