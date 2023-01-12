class Solution:
    def isValidSudoku(self, board):

        result = False
        size = 9

        digits = { str(e) for e in range(1,10)}
        columns = [set() for _ in range(size)]
        rows = [set() for _ in range(size)]
        boxes = [set() for _ in range(size)]

        for r in range(size):
            for c in range(size):

                if board[r][c]=='.':
                    continue

                if board[r][c] not in digits:
                    return result

                b = (size//3)*(r//(size//3))+(c//(size//3))
                if board[r][c] in columns[c] or board[r][c] in rows[r] or board[r][c] in boxes[b]:
                    return result
                
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[b].add(board[r][c])

            
        result = True
        return result
        







        return result