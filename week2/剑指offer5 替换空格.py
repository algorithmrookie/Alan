# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "We are happy."
# 输出："We%20are%20happy." 
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 10000 
#  Related Topics 字符串 
#  👍 148 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def replaceSpace(self, s: str) -> str:
        results = []
        for i in s:
            if i == " ":results.append('%20')
            else:results.append(i)
        return "".join(results)
# leetcode submit region end(Prohibit modification and deletion)

