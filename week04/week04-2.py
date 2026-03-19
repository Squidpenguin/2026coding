#week04-2.py
#1732
#找到最高的海拔高度
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain) #陣列長度
        ans = H = 0
        for i in range(N):
            H += gain[i]
            ans = max(ans,H)
        return ans
