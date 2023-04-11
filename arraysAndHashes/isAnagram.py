# return if s and t are the same length and have the same letters
# check if the length of s and t are the same
# check if s contains t
# make two hashes that will have s and t character values put into them
# those values count up for each time existing
# loop through one hash and check if its key value pairs have equal counts
# if they all have equality return true
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        evalAnaghram = False
        if len(s) == len(t):
            sLettersCount = Counter(s)
            tLettersCount = Counter(t)
            for letter in sLettersCount:
                if letter in tLettersCount and sLettersCount[letter] == tLettersCount[letter]:
                    evalAnagram = True
                else:
                    return False
            return evalAnagram
        else:
            return False
