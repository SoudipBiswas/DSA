class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Get the length of the input array
        n = len(nums)
        # Initialize the result list to store all unique quadruplets
        result = []
      
        # If array has less than 4 elements, no quadruplet possible
        if n < 4:
            return result
      
        # Sort the array to enable two-pointer technique and skip duplicates
        nums.sort()
      
        # First pointer: iterate through array leaving space for 3 more elements
        for i in range(n - 3):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
          
            # Second pointer: iterate from i+1 leaving space for 2 more elements
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
              
                # Use two pointers for the remaining two elements
                left = j + 1
                right = n - 1
              
                # Two-pointer approach to find pairs that sum to the remaining target
                while left < right:
                    # Calculate the sum of all four elements
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                  
                    if current_sum < target:
                        # Sum too small, move left pointer right to increase sum
                        left += 1
                    elif current_sum > target:
                        # Sum too large, move right pointer left to decrease sum
                        right -= 1
                    else:
                        # Found a valid quadruplet, add to result
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                      
                        # Move both pointers inward
                        left += 1
                        right -= 1
                      
                        # Skip duplicate values for the third element
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                      
                        # Skip duplicate values for the fourth element
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
      
        return result
