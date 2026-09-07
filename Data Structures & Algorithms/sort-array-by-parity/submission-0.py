'''
left = 0, 1
right = 3, 2
nums[left] = 3, 1
nums[right] = 4, 2 
output: nums[4, 1, 2, 3]
'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1

            elif nums[right] % 2 != 0:
                right -= 1

            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums

