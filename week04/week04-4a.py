#week04-4a.py (重寫week04-2.py)
#1732
#找到最高的海拔高度
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0
        for gg in gain:
            H += gg
            ans = max(ans,H)
        return ans
