from typing import List
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1]))

        lis_heights = [envelopes[0][1]]

        for width, height in envelopes[1:]:
            if height > lis_heights[-1]:

                lis_heights.append(height)
            else:

                insertion_index = bisect_left(lis_heights, height)
                lis_heights[insertion_index] = height
        return len(lis_heights)
