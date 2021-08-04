#剑指offer03

‘’‘
找出数组中重复的数字
 
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请
找出数组中任意一个重复的数字。 

’‘’


‘’‘
解题思路

这个题可以新建一个字典 dict_new ,然后遍历数组中的数，如果没出现就记录为 dict_new[nums[i]] = 1,如果字典中已经有了这个数，那就直接输出
由于新建了一个新的字典，所以空间复杂度是n，遍历了数组，时间复杂度是n

下面的解法是只需要进行遍历数组，然后直接在原数组上进行改变，空间复杂度将为1
‘’‘
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
