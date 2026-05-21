#week13-3.py
#215
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #nums.sort(reverse=True)
        #return nums[k-1]
        #Heap¸ê®Æµ²ºc
        #heapify(nums)
        #while nums:
            #print(heappop(nums))

        heapify(nums)
        for i in range(len(nums)-k):
            heappop(nums)
        return heappop(nums)
