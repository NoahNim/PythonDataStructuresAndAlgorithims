# return the two numbers in the array that added equal target
# make an empty array that will have the indexes
# make a hash
# loop through nums and check if value at index is in hash
# otherwise put it in as hash[target -val]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashObj = {}

        for index, value in enumerate(nums):
            if value in hashObj:
                return [hashObj[value], index]
            else:
                hashObj[target - value] = index
