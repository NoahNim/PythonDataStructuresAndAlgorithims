class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            middle = len(nums) // 2
            left = nums[:middle]
            right = nums[middle:]

            left = self.sortArray(left)
            right = self.sortArray(right)

            new_list = []

            while len(left) > 0 and len(right) > 0:
                if left[0] >= right[0]:
                    new_list.append(right.pop(0))
                else:
                    new_list.append(left.pop(0))
            new_list = new_list + left + right
            return new_list
        else:
            return nums
