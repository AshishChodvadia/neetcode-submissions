'''
Input: 2 strings
Output: True/False

Edge cases:
case sensitive, remove alnumeric

Process:
1. lower cases
2. strip whitespaces
3. remove numeric
4. two pointers approach left and right
5. Make sure both pointer values are not numeric
6. if any pointer value is whitespace then what
7. if any pointer value is nums then what
left=
right=
s[left]=
s[right]=
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        s = s.lower().strip()
        
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
            