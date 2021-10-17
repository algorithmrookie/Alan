class Solution:
    def validPalindrome(self, s):
        def check(l, r):
            while l <= r:
                if s[l] != s[r]:
                    break
                l += 1
                r -= 1
            return l, r

        mid = len(s) // 2
        left, right = check(0, len(s) - 1)
        if left > mid:
            return True
        return check(left + 1, right)[0] > mid or check(left, right - 1)[0] == mid
