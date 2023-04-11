# make an empty array
# make a hash that counts each element
# sort that hash from greatest to least
# push sortedNums elements into the empty array until array length is equal to k
# return that final array

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqArray = []
        hashNums = Counter(nums)
        sortedNums = sorted(hashNums, key=hashNums.get, reverse=True)

        for number in sortedNums:
            if len(freqArray) < k:
                freqArray.append(number)
            else:
                break
        return freqArray
