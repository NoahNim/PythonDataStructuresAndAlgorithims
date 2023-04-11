# if a number appears twice return true
# make a dictionary to put numbers as keys and values as counts
# if the numnber appears more than once return true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsCount = {}
        for number in nums:
            if number in numsCount:
                return True
            else:
                numsCount[number] = 1
        return False
