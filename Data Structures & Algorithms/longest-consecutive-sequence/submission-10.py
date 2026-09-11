class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)   #numsets=(20,2,4,10,3,4,5)
        sequence_count = 0
        max_count = 0

        for num in numset: #20
            if (num - 1) not in numset:#19
                sequence_count = 1
                next_num = num

                while (next_num + 1) in numset:
                    next_num += 1
                    sequence_count += 1
                max_count = max(sequence_count, max_count)
        
        return max_count

        '''
        if not nums:
        return 0

        nums.sort()
        longest = 1
        current_streak = 1
    
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # duplicate, doesn't break or extend the streak
            elif nums[i] == nums[i - 1] + 1:
                current_streak += 1  # streak continues
            else:
                current_streak = 1  # streak broken, start fresh at 1 (this number itself)
    
            longest = max(longest, current_streak)
    
        return longest
        '''



       
    