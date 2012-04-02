#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
import os, sys, argparse

class FileContextManager():
    def __init__(self,file_name):
        self._file_name = file_name
        self._file = None

    def __enter__(self):
        self._file = open(self._file_name)
        return self._file

    def __exit__(self,cls, value, tb):
        self._file.close()

def accessfile(file_name):
    with FileContextManager(file_name) as file:
        for line in file.readlines():
            getMissingLetters(line)
    pass

def getMissingLetters(sentence):

    alphabet = map(chr, range(97,123))
    sentence = sentence.lower()
    sentence = sentence.replace(' ','')
    result  = []

    for letter in alphabet:
        if letter not in sentence:
            result.append(letter)

    if len(result) > 0:
        print ''.join(result)
    else :
        print "NULL"

def main():
    if len(sys.argv) != 3:
        print "usage: ./string_utils.py command filename"
        sys.exit(1)

    filename = sys.argv[2]

    accessfile(filename)

if __name__ == '__main__':
    main()
