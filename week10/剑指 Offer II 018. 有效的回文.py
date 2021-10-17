class Solution:
    def isPalindrome(self, s):
        left, right, flag = 0, len(s) - 1, False
        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum() and right > left:
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
