class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for r in range(n):
            for c in range((n+1)//2):
                image[r][c], image[r][n-1-c] = image[r][n-1-c] ^ 1, image[r][c] ^ 1
                
        return image