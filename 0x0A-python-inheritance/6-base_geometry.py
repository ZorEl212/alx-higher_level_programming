#!/usr/bin/python3
"""class BaseGeometry w no area"""


class BaseGeometry:
    """No area for now"""
    def area(self):
        raise Exception('area() is not implemented')
