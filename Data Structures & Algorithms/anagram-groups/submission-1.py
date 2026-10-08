class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen =  defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord("a")] += 1
            seen[tuple(key)].append(word)
        result = [words for words in seen.values()]
        return result