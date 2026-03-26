#week05-4.py
#3546
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum([sum(row) for row in grid])
        presum = 0
        for row in grid:
            presum += sum(row)
            if total -presum == presum:
                return True

        presum = 0
        for col in zip(*grid):
            presum += sum(col)
            if total - presum == presum:
                return True

        return False
