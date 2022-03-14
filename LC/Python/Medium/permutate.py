from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perms = deque()
        perms.append([])
        
        for num in nums:
            for _ in range(len(perms)):
                old_perm = perms.popleft()
                
                for j in range(len(old_perm) + 1):
                    new_perm = list(old_perm)
                    new_perm.insert(j, num)
                    if len(new_perm) == len(nums):
                        ans.append(new_perm)
                    else:
                        perms.append(new_perm)
                        
        return ans