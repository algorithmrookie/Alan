class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right,sum,min_length = 0,0,0,float('inf')
        for right in range(len(nums)):
            sum += nums[right]
            while left <= right and sum >= target:
                min_length = min(min_length,right-left+1)
                sum -= nums[left]
                left += 1

        return 0 if min_length>len(nums) else min_length
