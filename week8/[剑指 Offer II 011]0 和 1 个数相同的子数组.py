# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。 
# 
#  示例 2: 
# 
#  
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] 不是 0 就是 1 
#  
# 
#  
# 
#  注意：本题与主站 525 题相同： https://leetcode-cn.com/problems/contiguous-array/ 
#  Related Topics 数组 哈希表 前缀和 👍 10 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dictx = {}
        dictx[0] = -1
        sumNums,maxLength = 0,0
        for i in range(0,len(nums)):
            if nums[i] == 0: nums[i] = -1
            sumNums += nums[i]
            if sumNums in dictx:maxLength = max(maxLength,i-dictx[sumNums])
            else:dictx[sumNums] = i
        return maxLength

# leetcode submit region end(Prohibit modification and deletion)
