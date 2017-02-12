#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

import svgwrite
import colorbrewer

from character_colors import colors

def list_json_files():
    return os.listdir('./json/')

def load_json_data(file_name):
    return json.load(open(file_name, 'r'))

def y_position(count, offset):
    return count + offset

def get_character_list(data_array):
    characters = []
    for line in data_array:
        characters.append(line['speaker'])
    return set(characters)

def process_data(json_file_name):
    svg_file_name = 'svg/' + json_file_name[:-4] + 'svg'
    romeo_array = load_json_data('json/' + json_file_name)
    drawing = svgwrite.Drawing(svg_file_name, size=(550, 1000), profile='tiny')
    x_offset = 0
    y_offset = 0
    act = ''
    scene = ''
    characters = get_character_list(romeo_array)
    character_colors = {}
    _colors = list(colors*3) # copy the colors list so we can pop off of it
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
            act_group.translate(x_offset, -y_position(count, y_offset))
            x_offset += 100


        if line['scene'] != scene:
            y_offset += 3
            act_group.add(drawing.line(
                (5, y_position(count, y_offset)),
                (95, y_position(count, y_offset)),
                stroke='blue'
            ))
            scene = line['scene']

        if line['speaker'] not in character_colors:
            character_colors[line['speaker']] = _colors.pop()

        svg_line = act_group.add(drawing.line(
            (10, y_position(count, y_offset)),
            (90, y_position(count, y_offset)),
            stroke=character_colors[line['speaker']],
        ))
    drawing.save()

def main():
    for json_file_name in list_json_files():
        process_data(json_file_name)

if __name__ == "__main__":
    main()
