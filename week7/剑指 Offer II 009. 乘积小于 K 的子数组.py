class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = ret = 0
        total = 1
        for right, num in enumerate(nums):
            total *= num
            while left <= right and total >= k:
                total //= nums[left]
                left += 1
            if left <= right:
                ret += right - left + 1
        return ret
