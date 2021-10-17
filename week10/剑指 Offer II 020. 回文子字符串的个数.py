class Solution:
    def countSubstrings(self, s: str)->int:
        length = len(s)
        dp = [0]*length #一维数组
        count = 0
        for j in range(length):         #j定的是每个被比较的字符
            for i in range(j+1):        #i<=j, i和j及j之前的比较，而此时的dp[i+1]其实就是dp[i+1][j-1]
                if s[i]==s[j] and (j-i<=2 or dp[i+1]):
                    dp[i] = True
                    count+=1
                else:
                    dp[i]=False
        return count
