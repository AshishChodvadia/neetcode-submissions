'''
num_set = set(nums)

        for num in range(len(nums) + 1):
            if num not in num_set:
                return num
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected = n * (n + 1) // 2
        return expected - sum(nums)