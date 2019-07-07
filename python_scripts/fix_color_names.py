#! /usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "MrJohnny786"


class Fixer(object):
    def __init__(self):
        self.colors_path = '/home/mrjohnny786/microservices/practice/congenial-octo-winner/resources/colors.txt'
        self.new_colors = []
        self.fixed_colors_path = '/home/mrjohnny786/microservices/practice/congenial-octo-winner/resources/fixed_colors.txt'

    def remove_color_codes(self, data):
        for color in data:
            _color = color.split()
            if len(_color) == 1:
                col = ''.join(_color)
                self.new_colors.append(col)
            elif _color[0] != 'Name':
                fixed_color = _color[:-1]
                fixed_color = ' '.join(fixed_color).lower()
                self.new_colors.append(fixed_color)
            else:
                continue

        return True

    def create_new_file(self, data):

        new_file = open(self.fixed_colors_path, 'w')
        for color in data:
            new_file.write(color + "\n")

        return True

    def main(self):
        try:
            colors_file = open(self.colors_path, 'r')
        except FileNotFoundError:
            raise Exception('No file found :(')
        if not self.remove_color_codes(colors_file):
            raise Exception("Something went wrong")
        self.create_new_file(self.new_colors)


if __name__ == '__main__':
    Fixer().main()
