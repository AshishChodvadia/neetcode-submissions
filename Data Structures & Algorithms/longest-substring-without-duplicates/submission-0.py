class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        unique = set()
        left = 0

        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1

            window_len = right - left + 1
            longest = max(longest, window_len)
            unique.add(s[right])
            
        return longest
