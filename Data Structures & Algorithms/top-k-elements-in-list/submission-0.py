class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        temp = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            frequency[num] += 1
        for x, y in frequency.items():
            temp[y].append(int(x))
        result = []
        for z in temp[::-1]:
            if len(result) < k:
                result.extend(z)
        return result