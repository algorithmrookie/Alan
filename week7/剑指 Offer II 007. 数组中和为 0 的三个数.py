class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        if len(nums)>=3: nums.sort()
        i = 0
        while i < len(nums)-2:
            self.twoSum(nums,i,results)
            temp = nums[i]
            while i < len(nums) and nums[i] == temp:
                i += 1
        return results

    def twoSum(self,nums,i,result):
        j,k = i+1,len(nums)-1
        while j < k:
            if nums[i] + nums[k] + nums[j] == 0:
                result.append([nums[i],nums[j],nums[k]])

                temp = nums[j]
                while nums[j] == temp and j < k:
                    j += 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1
