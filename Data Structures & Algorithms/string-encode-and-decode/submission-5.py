class Solution:

    def encode(self, strs: List[str]) -> str:
        output_list= []
        for word in strs:
            output_list.append(str(len(word)) + "#" + word)
        return "".join(output_list)

    def decode(self, s: str) -> List[str]:
        # last_index = 0
        output = []
        # for index, char in enumerate(s):
        #     if char == "#":
        #         length = int(s[last_index:index])
        #         output.append(s[index + 1: index + 1 + length])
        #         last_index = index + length + 1
        #         if last_index >= len(s):
        #             break
        if len(s) == 1:
            return output
        i = 0
        while i < len(s):
            deli = s.find("#", i)
            length = int(s[i:deli])
            output.append(s[deli + 1: deli + 1 + length])
            i = deli + length + 1
        return output
                