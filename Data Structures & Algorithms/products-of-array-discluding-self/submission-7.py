class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix  # product of nums[:i]
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix  # times product of nums[i+1:]
            suffix *= nums[i]
        return result
