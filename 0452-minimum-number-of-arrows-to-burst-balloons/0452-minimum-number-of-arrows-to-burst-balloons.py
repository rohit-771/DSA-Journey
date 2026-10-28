class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        ending= -float('inf')
        points.sort()
        arrow=0
        for start, end in points:
            if start<=ending:
                ending = min(ending, end)
            else:
                arrow+=1
                ending=end
        return arrow
