import pandas as pd
from keras.models import Sequential
from keras.layers import *
import csv
import re

PERMITTED_CHARS = "abcdefghijklmnopqrstuvwxyz"


def char_to_int(inputName):
    new_line = ""
    charind = 0
    for char in inputName:
        if char == 'a':
            charind = 0
        elif char == 'b':
            charind = 1
        elif char == 'c':
            charind = 2
        elif char == 'd':
            charind = 3
        elif char == 'e':
            charind = 4
        elif char == 'f':
            charind = 5
        elif char == 'g':
            charind = 6
        elif char == 'h':
            charind = 7
        elif char == 'i':
            charind = 8
        elif char == 'j':
            charind = 9
        elif char == 'k':
            charind = 10
        elif char == 'l':
            charind = 11
        elif char == 'm':
            charind = 12
        elif char == 'n':
            charind = 13
        elif char == 'o':
            charind = 14
        elif char == 'p':
            charind = 15
        elif char == 'q':
            charind = 16
        elif char == 'r':
            charind = 17
        elif char == 's':
            charind = 18
        elif char == 't':
            charind = 19
        elif char == 'u':
            charind = 20
        elif char == 'v':
            charind = 21
        elif char == 'w':
            charind = 22
        elif char == 'x':
            charind = 23
        elif char == 'y':
            charind = 24
        elif char == 'z':
            charind = 25

        if new_line == "":
            new_line = str(charind)
        else:
            new_line = new_line + ',' + str(charind)

    return new_line


def nametonum(file_to_open, file_to_write):
    training_data_df = pd.read_csv(file_to_open)
    new_file = open(file_to_write, 'a')

    for names in training_data_df.get_values():
        formattedNames = char_to_int("".join(c for c in str(names).lower() if c in PERMITTED_CHARS)) + "\n"
        new_file.write(formattedNames)
    new_file.close()


nametonum("NameListTesting.csv", "name_to_num.csv")
