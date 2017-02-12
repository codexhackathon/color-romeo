#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import xml.etree.ElementTree as ET

from textblob import TextBlob

def parse_xml():
    tree = ET.parse('./romeo_and_juliet_moby.xml')
    root = tree.getroot()
    acts = root.findall('ACT')
    romeo_array = []
    for act in acts:
        mor scene in act.findall('SCENE'):
            for speech in scene.findall('SPEECH'):
                for line in speech.findall('LINE'):
                    line_text = ''
                    for ll in line.itertext():
                        line_text = line_text + ll

                    # Generate text statistics
                    text_blob = TextBlob(line_text)

                    # Generate list of matches of time words
                    matches = match_time_words_in_string(line_text)

                    romeo_array.append({
                        'act': act.find('TITLE').text,
                        'scene': scene.find('TITLE').text,
                        'speaker': speech.find('SPEAKER').text,
                        'line': line_text,
                        'line_polarity': text_blob.sentiment.polarity,
                        'line_subjectivity': text_blob.sentiment.subjectivity,
                        'matches': matches
                    })

    return romeo_array

def match_time_words_in_string(line):
    # Takes a line of shakespere and matches it to a word describing time
    matches = []
    matching_words = [
        'morrow', 'absent', 'absence', 'brief', 'consequence', 'continu',
        'dark', 'day', 'death', 'early', 'end', 'expire', 'haste',
        'hour', 'long', 'mend', 'minute', 'miss', 'moon', 'morn',
        'old', 'pass', 'sun', 'tardy', 'term', 'time', 'young'
        ]
    for match_word in matching_words:
        if match_word in line.lower():
            matches.append(match_word)
    return matches


if __name__ == "__main__":
    romeo_array = parse_xml()

    with open('romeo_analysis_array.json', 'w') as romeo_file:
        json.dump(romeo_array, romeo_file, indent=4)
