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
            mem = [[-1]*100]*100
            lcs_score = memo_lcs(line_in, i, len(line_in), len(i), mem)
            words_consider.append((lcs_score, i))

    longest_word = max(words_consider)
    return longest_word


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


def lcs_memo(f):
    '''
    Memoized function decorator 
    '''
    memo = [[-1]*100]*100

    def inner(s1, s2, l1, l2):
        memo[l1 - 1][l2 - 1] = f(s1, s2, l1, l2)
    
    return inner

@lcs_memo
def lcs(s1, s2, l1, l2):
    '''
    Naive recursive implementation of longest common subsequence
    exit on length of either string hitting zero
    if characters at given index match, return 1 + next round of lcs
    if characters don't match, return the max of the next rounds of lcs for two directions

    Bug
    '''
    if l1 == 0 or l2 == 0:
        return 0
    
    if s1[l1 - 1] == s2[l2 - 1]:
        # bug occuring here
        return 1 + lcs(s1, s2, l1 - 1, l2 - 1)
    else:
        return max(lcs(s1, s2, l1, l2 - 1), lcs(s1, s2, l1 - 1, l2))
    

def memo_lcs(s1, s2, l1, l2, mem):
    '''
    memoized longest common subsequence
    '''
    if l1 == 0 or l2 == 0:
        return 0
    
    if mem[l1 -1][l2 - 1] != -1:
        return mem[l1 -1][l2 - 1]
    
    if s1[l1 - 1] == s2[l2 - 1]:
        mem[l1 - 1][l2 - 1] = 1 + memo_lcs(s1, s2, l1 - 1, l2 - 1, mem)
        return mem[l1 - 1][l2 - 1]
    else:
        mem[l1 - 1][l2 -1] = max(memo_lcs(s1, s2, l1, l2 - 1, mem), memo_lcs(s1, s2, l1 - 1, l2, mem))
        return mem[l1 - 1][l2 - 1]


if __name__ == "__main__":
    longest = main(sys.argv)
    print(longest)
