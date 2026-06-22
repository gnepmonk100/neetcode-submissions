class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # intuitively, this must be O(n^2) because you have to check 1 through N for each column/row 
        # and there are N rows/columns 


        # Firstly, check each column
        for idx_i in range(9):
            seen = []
            for idx_j in range(9):
                if board[idx_i][idx_j] == '.':
                    continue
                elif board[idx_i][idx_j] in seen:
                    return False
                else:
                    seen.append(board[idx_i][idx_j])

        # Then, check each row
        for idx_j in range(9):
            seen = []
            for idx_i in range(9):
                if board[idx_i][idx_j] == '.':
                    continue
                elif board[idx_i][idx_j] in seen:
                    return False
                else:
                    seen.append(board[idx_i][idx_j])
        # Finally, check each 3x3 box
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = set() # Using a set is O(1) for lookups!
                # Iterate through the 3x3 area
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        val = board[i][j]
                        if val == '.':
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
                        
        return True
        