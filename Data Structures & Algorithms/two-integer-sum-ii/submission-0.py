'''
numbers = [10, 11, 12, 13, 14]
target = 25
my_list = {}
left = 0
right = 4
numbers[left] = 10
numbers[right] = 14
total = 24

left = 1
right = 4
numbers[left] = 11
numbers[right] = 14
total = 25

left = 2
right = 4
numbers[left] = 12
numbers[right] = 14
total = 26

left = 2
right = 3
numbers[left] = 12
numbers[right] = 13
total = 25

left = 0
right = len(numbers) - 1

while left < right:
    total = numbers[left] + numbers[right]
    if total > target:
        right -= 1
    elif total < target:
        left += 1 
    elif total = target:
        return [left, right]

'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1 
            elif total == target:
                return [left + 1, right + 1]

    