class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        counter = 1
        
        for n in nums_set:
            if n - 1 not in nums_set and n + 1 in nums_set:
                start = n
                temp_counter = 1
                while start + 1 in nums_set:
                    temp_counter += 1
                    start += 1
                counter = max(counter, temp_counter)
        return counter