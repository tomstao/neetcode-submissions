class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height) - 1
        res = 0
        l_max, r_max = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                l_max = max(height[l], l_max)
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(height[r], r_max)
                res += r_max - height[r]
        return res