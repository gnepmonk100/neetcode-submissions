class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row_num in range(len(matrix)):

            left = 0
            right = len(matrix[0]) - 1

            while left <= right:
                M = (left + right) // 2
                if matrix[row_num][M] == target:
                    return True
                elif matrix[row_num][M] >= target:
                    right  = M-1
                else:
                    left = M + 1

        return False


        