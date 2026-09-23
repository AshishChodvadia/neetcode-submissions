class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        left = 0
        for right in range(len(s2)):
            left = right - len(s1) + 1
            #if left < 0:
            #   continue
            if sorted(s1) == sorted(s2[left:right + 1]):
                return True

        return False