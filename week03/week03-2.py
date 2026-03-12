#week03-2.py
#643
#找到長度k的最小陣列(平均最大) 找到total最大即可
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
        total = sum(nums[:k])
        maxTotal = total
        for i in range(k,N):
            total = total + nums[i] - nums[i-k]
            maxTotal = max(maxTotal, total)
        return maxTotal/k
