'''
letter = n, e, e, t, c, o
result_string = "no"
pointer = 0, 1, 2
s[pointer] = n, o, d
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (s == t) or (s == "" and t != ""):
          return True

        #result_string = ""
        pointer = 0
        for letter in t:
            if pointer < len(s) and letter == s[pointer] :
                #result_string += letter
                pointer += 1

        #return result_string == s
        return pointer == len(s)
            

