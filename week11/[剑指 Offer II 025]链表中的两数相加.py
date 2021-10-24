# 给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。 
# 
#  可以假设除了数字 0 之外，这两个数字都不会以零开头。 
# 
#  
# 
#  示例1： 
# 
#  
# 
#  
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
#  
# 
#  示例2： 
# 
#  
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
#  
# 
#  示例3： 
# 
#  
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 100] 
#  0 <= node.val <= 9 
#  输入数据保证链表代表的数字无前导 0 
#  
# 
#  
# 
#  进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。 
# 
#  
# 
#  注意：本题与主站 445 题相同：https://leetcode-cn.com/problems/add-two-numbers-ii/ 
#  Related Topics 栈 链表 数学 👍 13 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        return pre

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rev_l1 = self.reverseList(l1)
        rev_l2 = self.reverseList(l2)
        count = 0
        ret = ListNode()
        tmp = ret
        while rev_l1 or rev_l2 or count:
            num = 0
            if rev_l1:
                num += rev_l1.val
                rev_l1 = rev_l1.next
            if rev_l2:
                num += rev_l2.val
                rev_l2 = rev_l2.next
            count, num = divmod(num + count, 10)
            tmp.next = ListNode(num)
            tmp = tmp.next
        return self.reverseList(ret.next)



# leetcode submit region end(Prohibit modification and deletion)
