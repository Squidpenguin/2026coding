# week01-4.py(還未上傳)
# 1431
# 判斷是不是最多的
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        best = max(candies)
        for candie in candies:
            if candie + extraCandies >= best:
                ans.append(True)
            else:
                ans.append(False)
        return ans
