'''
nums = [0, 1, 3]
lower = 0
upper = 5
missing = 2, 4, 5.
missing = 0, 1, 2, 3, 4
missing has to start somewhere
num = 0, 1, 3

output: my_list = [[2,2], ]

Loop through 1 to 3:
    Give me first number after 1 and give me number before 3 [2, 2]

Loop through 3 to 5:
    [4, 4]

    num = 
'''

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        my_list = []
        missing = lower
        for num in nums:
            if missing < num:
                my_list.append([missing, num - 1])
           
            missing = num + 1

        if missing <= upper:
            my_list.append([missing, upper])

        return my_list

