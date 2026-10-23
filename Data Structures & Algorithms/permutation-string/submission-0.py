from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        if len(s1) > len(s2):
            return False
        r = 0
        for l in range(len(s2)):
            r = l + len(s1)
            count_s2 = Counter(s2[l:r])

            if count_s2 == count:
                return True
            l += 1
        return False