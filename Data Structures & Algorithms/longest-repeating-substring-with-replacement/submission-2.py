from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c_dict = {}
        l = 0
        max_l = 0
        for r in range(len(s)):
            c_dict[s[r]] = 1 + c_dict.get(s[r], 0)

            if r - l + 1 - max(c_dict.values()) > k:
                c_dict[s[l]] -= 1
                l += 1
                continue
            max_l = max(max_l, r - l + 1)

        return max_l