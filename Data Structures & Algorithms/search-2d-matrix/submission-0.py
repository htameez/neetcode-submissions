class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do binary search on each row, where each row is a range of numbers [x, y]
        # if target is greater than y, go to next row 
        # if target is less than y, search that row by making new range and repeating
        
        top = 0
        bottom = len(matrix) - 1

        # Find the row whose range contains target
        while top <= bottom:
            row = top + (bottom - top) // 2

            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        else:
            # No row's range contains target
            return False

        # Search within the selected row
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False
                