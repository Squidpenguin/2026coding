#week02-2.py(還沒上傳)
#283
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        N = len(nums)
        k = 0
        for i in range(N):
            if nums[i] != 0: #遇到不是0 搬到左邊
                nums[k] = nums[i] #左nums[k] 右nums[i]
                k += 1

        for i in range(k,N): #剩下格子補0
            nums[i] = 0
