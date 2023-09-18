#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """Print text based on some rules."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    ptext = []
    puncutations = [".", "?", ":"]
    for char in range(len(text)):
        if text[char] == " " and (len(ptext) == 0 or ptext[-1] in puncutations
                                  or text[char-1] == "\n"):
            continue
        if text[char] in puncutations:
            print(text[char])
            ptext.append(text[char])
            print()
            continue
        print(text[char], end="")
        ptext.append(text[char])
