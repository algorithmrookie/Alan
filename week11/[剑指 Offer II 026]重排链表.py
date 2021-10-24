# 给定一个单链表 L 的头节点 head ，单链表 L 表示为： 
# 
#  L0 → L1 → … → Ln-1 → Ln 
# 请将其重新排列后变为： 
# 
#  L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → … 
# 
#  不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: head = [1,2,3,4]
# 输出: [1,4,2,3] 
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: head = [1,2,3,4,5]
# 输出: [1,5,2,4,3] 
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 5 * 10⁴] 
#  1 <= node.val <= 1000 
#  
# 
#  
# 
#  注意：本题与主站 143 题相同：https://leetcode-cn.com/problems/reorder-list/ 
#  Related Topics 栈 递归 链表 双指针 👍 13 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        vec = list()
        node = head
        while node:
            vec.append(node)
            node = node.next

        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1

        vec[i].next = None

# leetcode submit region end(Prohibit modification and deletion)
