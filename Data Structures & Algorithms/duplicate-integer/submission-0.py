class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while nums:
            temp = nums.pop(0)
            if temp in nums:
                return True
        return False