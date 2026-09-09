'''
input/output: array/array
example:
brute force

'''
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {} #num:count
        heap = []
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        heap = []
        for num, count in frequency.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]