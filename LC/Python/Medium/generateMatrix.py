class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res, curr = [[0]*n for _ in range(n)], 0
        for i in range(n>>1):
            for j in range(i, n-i):
                res[i][j] = (curr := curr+1)
            for j in range(i+1, n-i):
                res[j][-i-1] = (curr := curr+1)
            for j in range(i+1, n-i):
                res[-i-1][-j-1] = (curr := curr+1)
            for j in range(i+1, n-i-1):
                res[-j-1][i] = (curr := curr+1)
        if n&1:
            res[n>>1][n>>1] = curr+1
        return res