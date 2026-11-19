class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows, cols = 9 , 9
        for lis in board:
            freq= {}
            for num in lis:
                freq[num] = freq.get(num, 0) + 1

            for i in range(1,10):
                if freq.get(str(i), 0) > 1 :
                    return False

        for j in range(cols):
            freq = {}
            for i in range(rows):
                freq[board[i][j]] = freq.get(board[i][j], 0) + 1

            for z in range(1,10):
                if freq.get(str(z), 0) > 1 :
                    return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                freq = {}
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        val = board[i][j]
                        if val != ".":
                            if val in freq:
                                return False
                            freq[val] = 1
        

        return True