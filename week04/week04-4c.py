#week04-4c.py (重寫week04-4b.py)
#3866
#找到陣列 nums裡只出現過1次的偶數 第一次出現的位置
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = Counter(nums)
        for nn in nums:
            if nn%2 == 0 and H[nn] ==1:
                return nn
        return -1
