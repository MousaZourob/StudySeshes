class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False 
        
        top, bot = 0, len(matrix)-1
        while bot >= top:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else: 
                break
        
        if not bot >= top:
            return False
        
        row = (top + bot) // 2
        l, r = 0, len(matrix[0])-1
        while r >= l:
            m = (r + l) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False