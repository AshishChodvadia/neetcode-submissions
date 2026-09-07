'''
abbda
 l
   r  
is left = right?
yes: left += 1, right -= 1

move left += 1 if left = right
else move right -= 1 if left = right

matching
1. 

not matching
1. skip left s[l + 1:r + 1] - match?
OR
2. skip right s[l:r] - match?
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                skipL = s[left + 1:right + 1]
                skipR = s[left:right]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
        return True

        