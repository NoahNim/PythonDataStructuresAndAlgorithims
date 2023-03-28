from collections import deque

# ([]{}) is also a valid string
# make a variable to store booplean state
# check if the string is empty, return false if it is
# make a hashMap to store bracketing info in
# create a list that will be the stack, add the last character of the string to it
# make a while loop for while the stack isn't empty
# make a variable called current which is stack.pop()
# make a variable called next which is the element before current as it will be popped next
# make a variable that's the first element
# check if next is the closing of current, if it's not check if first is
# if current is a ({[ pop it and move on to the mext


class Solution:
    def isValid(self, s: str) -> bool:
        myBool = False
        boolChecked = False
        hashMap = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        if len(s) == 0 or len(s) == 1:
            return False
        stack = deque(s)
        previous = None
        if stack[len(stack) - 1] not in hashMap:
            return False
        # while stack:

        return myBool
