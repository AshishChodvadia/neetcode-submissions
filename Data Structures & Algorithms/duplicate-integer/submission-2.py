class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return True

        return False

        '''
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == nums[right]:
                return True

            left += 1
            right -= 1
            

        return False
'''
        '''
        my_dict = {}
        for num in nums:
            if num in my_dict:  #{1:1, 2:1, 3:2}
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        for num in my_dict.values():
            if num > 1:
                return True

        return False
        '''
'''
left=0
right=3
nums[left]=1
nums[right]=4

left=1
right=3
nums[left]=2
nums[right]=4

left=2
right=3
nums[left]=3
nums[right]=4

'''
        

