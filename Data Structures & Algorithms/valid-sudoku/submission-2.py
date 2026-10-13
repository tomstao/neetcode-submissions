class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nums = "".join(row).replace(".", "")
            if len(nums) != len(set(nums)):
                return False
        for col in range(9):
            nums = []
            for row in range(9):
                nums.append(board[row][col])
            nums_str = "".join(nums).replace(".", "")
            if len(nums_str) != len(set(nums_str)):
                return False
        for i in range(0, 9, 3):
            for l in range(0, 9, 3):
                nums = []

                for j in range(i, i + 3):
                    for k in range(l, l + 3):
                        nums.append(board[j][k])
                nums_str = "".join(nums).replace(".", "")
                if len(nums_str) != len(set(nums_str)):
                    return False

        return True
