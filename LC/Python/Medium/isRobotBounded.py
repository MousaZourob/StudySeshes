class Solution(object):
    def isRobotBounded(self, I):
        di = x = y = 0
        for i in I:
            if i == 'L': di = (di + 1) % 4
            elif i == 'R': di = (di - 1) % 4
            else: 
                if di == 0:
                    y += 1
                elif di == 1:
                    x += 1
                elif di == 2:
                    y -= 1
                else:
                    x -= 1
                    
        if x == 0 and y == 0 or di > 0: return True
        return False