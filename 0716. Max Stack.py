"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""

# Time: O(n), Space: O(n).
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.maxStack or x >= self.maxStack[-1]:
            self.maxStack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.stack[-1] == self.maxStack[-1]:
            self.maxStack.pop()
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def peekMax(self):
        """
        :rtype: int
        """
        return self.maxStack[-1]
        

    def popMax(self):
        """
        :rtype: int
        """
        res = self.maxStack[-1]
        tmp = []
        while self.stack[-1] != res:
            tmp.append(self.stack.pop())
        # pop the max
        self.stack.pop() 
        self.maxStack.pop()
        while tmp:
            val = tmp[-1]
            self.stack.append(val)
            # CAUTION: need to place tmp elements back into maxStack as well!
            if not self.maxStack or val >= self.maxStack[-1]:
                self.maxStack.append(val)
            tmp.pop()
            
        return res

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
