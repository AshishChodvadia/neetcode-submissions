'''
Input: 2 strings
output: Boolean true/false

What do I need to traverse through?
--> Each letter of the both strings

What do I need to keep track of?
--> if each letter from string s is in string t or not

What are the edge cases?
--> Empty string, lower case, upper case, all letter or alphanumeric, special characters
--> What if string s has racecarr and string t has carrace, Do I need to handle that?

All if/else conditions:
1. Sort both strings will be list so convert it back to strings
2. if match return true else false
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_s = "".join(sorted(s))
        string_t = "".join(sorted(t))

        return string_s == string_t