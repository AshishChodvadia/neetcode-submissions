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



       
    