#week04-3.py
#3866
#找到陣列 nums裡只出現過1次的偶數 第一次出現的位置
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        N = len(nums)
        H = [0]*200
        for i in range(N):
            H[nums[i]] += 1
        for i in range(N):
            if nums[i]%2 == 0 and H[nums[i]] ==1:
                return nums[i]
        return -1
