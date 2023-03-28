# reverse and lowercase the string
# remove the non alphanumeric characters use translate
# lowercase inputstring and remove nonalphanum characters
# check if string reverse is the same as the lowrercased input string

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        sReverse = s[::-1].lower()
        sReverseAlpha = sReverse.translate(
            {ord(i): None for i in "!@#$%^&*():;_+-=`~ '',.<>?/\|[{]}''"})
        sReverseX = sReverseAlpha.replace('"', '')
        sLowered = s.lower()
        sLoweredAlpha = sLowered.translate(
            {ord(i): None for i in "!@#$%^&*():;_+-=`~ '',.<>?/\|[{]}''"})
        sLoweredX = sLoweredAlpha.replace('"', '')

        print(sLoweredX)
        print(sReverseX)

        if (sLoweredX == sReverseX):
            return True
        else:
            return False
