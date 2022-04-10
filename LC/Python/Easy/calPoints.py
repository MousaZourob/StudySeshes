class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        
        for o in ops:
            if o == '+':
                ans.append(ans[-1] + ans[-2])
            elif o == 'C':
                ans.pop()
            elif o == 'D':
                ans.append(ans[-1] * 2)
            else:
                ans.append(int(o))

        return sum(ans)