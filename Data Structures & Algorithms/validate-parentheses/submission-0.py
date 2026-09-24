class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []

        for brace in s:
            if brace in "{[(":
                stack.append(brace)
            else:
                if not stack or stack[-1] != valid[brace]:
                    return False
                stack.pop()

        return stack == []
                    