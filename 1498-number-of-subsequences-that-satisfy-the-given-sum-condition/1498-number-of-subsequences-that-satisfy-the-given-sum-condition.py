class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7

        nums.sort()
        n = len(nums)

        power_of_two = [1] * n
        for i in range(1, n):
            power_of_two[i] = (power_of_two[i - 1] * 2) % MOD

        result = 0
        for left_idx, min_val in enumerate(nums):
            if min_val * 2 > target:
                break
            max_allowed = target - min_val
            left = left_idx
            right = n - 1
            first_true_index = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > max_allowed:  
                    first_true_index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            right_idx = first_true_index - 1 if first_true_index != -1 else n - 1

            subsequence_count = power_of_two[right_idx - left_idx]
            result = (result + subsequence_count) % MOD

        return result
