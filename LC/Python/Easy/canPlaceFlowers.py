class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeros, counter = 1, 0
        for f in flowerbed:
            if f == 0: 
                zeros += 1
            else:
                counter += (zeros - 1) // 2
                zeros = 0
        return counter + zeros // 2 >= n