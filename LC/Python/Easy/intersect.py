class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = defaultdict(int)
        ans = []
        
        for num in nums1:
            count[num] += 1
        for num in nums2:
            if count.get(num):
                ans.append(num)
                count[num] -= 1

        return ans