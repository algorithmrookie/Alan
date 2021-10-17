class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        left = 0
        sub = []
        for i in range(len(s)):
            while s[i] in sub:
                sub.pop(0)
            sub.append(s[i])
            res = max(res, len(sub))
        return res
