'''
Given: int array
Track: index, Sum of elements in nums
Task
grab the left input
left = index
right = 
left = 0, 1, 2
right = 2
nums[left] = -2, 0, 3
sum = 0 + -2 + 0 + 3
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        while left <= right:
            total += self.nums[left]
            left += 1

        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)