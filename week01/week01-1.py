#week01-1.py
#案计//2 计+1 拜或跑1
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        n = int(s,2)
        while n>1:
            if n%2==0: n//=2
            else: n+=1
            ans += 1
        return ans
