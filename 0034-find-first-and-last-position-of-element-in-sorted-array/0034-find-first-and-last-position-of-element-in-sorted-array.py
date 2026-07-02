class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binarySearch(isLeftBias: bool) -> int:
            left, right = 0, len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    idx = mid
                    if isLeftBias:
                        right = mid - 1
                    else:
                        left = mid + 1
            return idx

        first = binarySearch(isLeftBias=True)
        last = binarySearch(isLeftBias=False)
        
        return [first, last]
