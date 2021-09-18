class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:return [-1,-1]
        left,right = 0,len(numbers)-1
        while left<right and numbers[left]+numbers[right] !=target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [left,right]
