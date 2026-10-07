class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for index, num in enumerate(nums):
            if target - num in seen:
                return [nums.index(target - num), index]
            seen.add(num)
