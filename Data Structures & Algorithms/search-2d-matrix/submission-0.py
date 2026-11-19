class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low = 0
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        high = rows*cols -1 

        while low <= high:
            mid = int(low + (high - low) / 2)

            row = int(mid / cols)
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False