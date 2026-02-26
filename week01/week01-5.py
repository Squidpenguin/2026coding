#week01-5.py(還沒上傳)
#238
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        preSum = [1] #左邊累積乘起來的值
        postSum = [1] #右邊累積乘起來的值
        for i in range (N):
            preSum.append(preSum[-1]*nums[i])
            postSum.append(postSum[-1]*nums[N-1-i])
        ans = []
        for i in range(N):
            ans.append(preSum[i]*postSum[N-1-i])
        return ans
