class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0 for _ in range(x)] for x in range(1, query_row + 2)]
        glasses[0][0] = poured
        
        for r in range(query_row):
            for c in range(r + 1):
                quant = (glasses[r][c] - 1) / 2.0
                if quant > 0:
                    glasses[r + 1][c] += quant
                    glasses[r + 1][c + 1] += quant
        
        return min(1, glasses[query_row][query_glass])