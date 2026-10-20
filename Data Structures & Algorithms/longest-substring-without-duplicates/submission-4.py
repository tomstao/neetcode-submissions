class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, max_l= 0, 1
        s_set = set()
        
        for r in range(len(s)):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            r += 1
            max_l = max(max_l, r - l)

        return max_l
