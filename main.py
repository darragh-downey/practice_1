#!/usr/bin/env python

import sys


def main(args):
    line_in = args[1]
    words = args[2:]

    line_in_count = char_count(line_in)
    words_count = {}
    words_consider = []

    for i in words:
        words_count[i] = char_count(i)

    for i in words_count:
        if compare(line_in_count, i, words_count[i]):
            words_consider.append(i)

    return max(words_consider)


def compare(line_in, word, word_count):
    '''
    compare line in with a given word, determine whether a word 
    can be generated from the letters in the string
    '''
    for k in word_count:
        if k not in line_in:
            return False
        elif word_count[k] > line_in[k]:
            return False
    return True


def char_count(line_in):
    '''
    Determine the number of occurances of a character in a string
    '''
    count = {}
    for i in line_in:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count


if __name__ == "__main__":
    longest = main(sys.argv)
