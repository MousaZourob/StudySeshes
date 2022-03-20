class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for target in [tops[0], bottoms[0]]:
            miss_t, miss_b = 0, 0
            for i in range(len(tops)):
                if not (target == tops[i] or target == bottoms[i]):
                    break
                if target != tops[i]: miss_t += 1
                if target != bottoms[i]: miss_b += 1
                if i == len(tops) - 1:
                    return min(miss_t, miss_b)
                
        return -1