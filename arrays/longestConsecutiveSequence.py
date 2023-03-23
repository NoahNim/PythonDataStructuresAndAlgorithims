# create a variable for longest consecutive count
# create a current count variable
# sort the array
# put each number of that array in a hash
# loop through array of hash, check if number - previous number == 1 if it does add to longest count abnd currentCount
# if a number - previous number isn't 1 reset current count to zero
# at the end of the loop if currentCount is greater than longestCount then return current Count
# else return longestCount

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longestCount = 1
        currentCount = 1
        previousLongest = 1
        sortedNums = sorted(nums)
        print(sortedNums)
        sortedHash = {}

        for number in sortedNums:
            if number not in sortedHash:
                sortedHash[number] = number

        sortedNumsSingles = list(sortedHash.values())

        for i in range(1, len(sortedNumsSingles)):
            if sortedNumsSingles[i] - sortedNumsSingles[i - 1] == 1:
                currentCount += 1
                longestCount += 1
            else:
                if previousLongest < longestCount:
                    previousLongest = longestCount
                longestCount = 1
                currentCount = 1

        if currentCount > previousLongest:
            return currentCount
        if previousLongest > longestCount:
            return previousLongest
        else:
            return longestCount
