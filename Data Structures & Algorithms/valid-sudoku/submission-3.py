class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        b = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                box = (row // 3) * 3 + col // 3
                if num in r[row] or num in c[col] or num in b[box]:
                    return False
                
                r[row].add(num)
                c[col].add(num)
                b[box].add(num)

        return True

                