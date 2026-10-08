from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        bucket = [[] for _ in range(max(frequency.values()) + 1)]
        for x, y in frequency.items():
            bucket[y].append(x)
        result = []
        for z in reversed(bucket):
            result.extend(z)
            if len(result) >= k:
                break
                
        return result