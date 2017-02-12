#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import svgwrite

characters = ["ABRAHAM", "Apothecary", "BALTHASAR", "BENVOLIO", "CAPULET",
        "First Citizen", "First Musician", "First Servant", "First Watchman",
        "FRIAR JOHN", "FRIAR LAURENCE", "GREGORY", "JULIET", "LADY CAPULET",
        "LADY MONTAGUE", "MERCUTIO", "MONTAGUE", "Musician", "Nurse", "NURSE",
        "PAGE", "PARIS", "PETER", "PRINCE", "ROMEO", "SAMPSON",
        "Second Capulet", "Second Musician", "Second Servant",
        "Second Watchman", "Servant", "Third Musician", "Third Watchman",
        "TYBALT"]
colors = [svgwrite.rgb(179,226,205), svgwrite.rgb(253,205,172),
        svgwrite.rgb(203,213,232), svgwrite.rgb(244,202,228),
        svgwrite.rgb(230,245,201), svgwrite.rgb(255,242,174),
        svgwrite.rgb(241,226,204), svgwrite.rgb(204,204,204),
        svgwrite.rgb(251,180,174), svgwrite.rgb(179,205,227),
        svgwrite.rgb(204,235,197), svgwrite.rgb(222,203,228),
        svgwrite.rgb(254,217,166), svgwrite.rgb(255,255,204),
        svgwrite.rgb(229,216,189), svgwrite.rgb(253,218,236),
        svgwrite.rgb(242,242,242), svgwrite.rgb(166,206,227),
        svgwrite.rgb(31,120,180), svgwrite.rgb(178,223,138),
        svgwrite.rgb(51,160,44), svgwrite.rgb(251,154,153),
        svgwrite.rgb(227,26,28), svgwrite.rgb(253,191,111),
        svgwrite.rgb(255,127,0), svgwrite.rgb(202,178,214),
        svgwrite.rgb(106,61,154), svgwrite.rgb(255,255,153),
        svgwrite.rgb(177,89,40), svgwrite.rgb(27,158,119),
        svgwrite.rgb(217,95,2), svgwrite.rgb(117,112,179),
        svgwrite.rgb(231,41,138), svgwrite.rgb(102,166,30),
        svgwrite.rgb(230,171,2), svgwrite.rgb(166,118,29),
        svgwrite.rgb(102,102,102)]
character_colors = dict(zip(characters, colors))
