class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #[1,7,2,5,4,7,3,6]
        # l             r
        # area = 1 * 7 = 7
        # max_units_water = 7
        #width=7-0=7
        #area=7
        left = 0
        right = len(heights) - 1
        max_units_water = 0
        
        while left < right:
            width = right - left
            area = min(heights[left], heights[right]) * width
            max_units_water = max(max_units_water, area)
            #can't think forward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_units_water