class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        ans = 0
        prevEnd = 0
        
        for _, end in intervals:
            if end > prevEnd:
                ans += 1
                prevEnd = end
                
        return ans
