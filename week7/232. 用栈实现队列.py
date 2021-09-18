class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):              # 入栈
        self.stack.append(x)

    def pop(self):                  # 出栈
        if self.is_empty:           # 注意特殊情况
            return None
        return self.stack.pop()

    @property
    def length(self):               # 获取栈中元素
        return len(self.stack)
    
    @property                      
    def is_empty(self):            # 获取栈的状态：是否为空
        return self.length == 0


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = Stack()                           # 基本栈
        self.stack2 = Stack()                           # 辅助栈

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.push(x)                             # 入栈，即入队列

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.stack1.length > 1:                   # 卡住要出栈的最后一个元素
            self.stack2.push(self.stack1.pop())         # 其他元素倒进辅助栈
        res = self.stack1.pop()                         # 那个被卡住的元素就是所需
        while not self.stack2.is_empty:                 # 只要辅助栈不为空
            self.stack1.push(self.stack2.pop())         # 辅助栈中的元素倒回基本栈
        return res                                      # 返回栈底元素即为出队队头

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.stack1.length > 1:                   # 卡住要出栈的最后一个元素
            self.stack2.push(self.stack1.pop())         # 其他元素倒进辅助栈
        res = self.stack1.pop()                         # 那个被卡住的元素就是所需
        self.stack2.push(res)                           # 记得把被卡住的元素放回
        while self.stack2.length > 0:                   # 只要辅助栈不为空
            self.stack1.push(self.stack2.pop())         # 辅助栈中的元素倒回基本栈
        return res                                      # 返回栈底元素即为出队队头

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack1.is_empty                     # 队列的状态即为基本栈的状态
