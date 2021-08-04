**剑指offer03**

**找出数组中重复的数字** 
 
#在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请
#找出数组中任意一个重复的数字。 

#时间复杂度是O（n），空间复杂度是1

class Solution:
  #def findRepeatNumber(self, nums: List[int]) -> int:
  def findRepeatNumber(self,nums):
      n = len(nums)
      nums.append(n)  # 0特殊处理，首先将nums数组后面加一个位置，将长度n变成n+1
      for i in range(len(nums)):
          if nums[i] == 0:
              nums[i] = n
          tmp = abs(nums[i])
          if nums[tmp] < 0 and tmp < n:
              return tmp
          elif nums[tmp] < 0 and tmp == n:
              return 0
          nums[tmp] *= -1

solution = Solution()
nums = [1,2,3,4,5,5,3,2]
print(solution.findRepeatNumber(nums))
