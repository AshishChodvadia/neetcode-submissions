'''
input: array of nums and target
output: indexes

What do I need to travaerse through?
index

What do I need to keep track of?
the sum of the two numbers from index value


Loop through index of nums
add the num to dictionary if num sum can be target
i = 0
nums[i]=3
needed =4
output/my_result = {3:0,}
range = 4

i = 1
nums[i]=4
needed =3
output/my_result = {3:0,}
range = 4

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_result = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed not in my_result:
                my_result[nums[i]] = i
            else:
                return [my_result[needed], i]

        return[-1, -1]
