import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        result = [0 for _ in range(len(nums))]
        if zero_count > 1:
            return result
        prod = math.prod(nums)

        if prod != 0:
            return [prod // num for num in nums]
        for index, num in enumerate(nums):
            if num == 0:
                new_prod = math.prod([num for num in nums if num != 0])
                result[index] = new_prod
        return result