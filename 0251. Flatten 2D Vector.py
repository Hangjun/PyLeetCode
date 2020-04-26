"""
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.

 

Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
 

Notes:

Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.
 

Follow up:

As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""

# The caveat here is to avoid empty list or end of list situations. We implement next() in a way that we always move the pointers 
# to the next feasible locations before extracting the element to return.
# Time: O(n), Space: O(n).
class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.v = v
        self.curRow = 0
        self.pos = 0
        

    def next(self):
        """
        :rtype: int
        """
        # Reset pointers
        self.hasNext()
        res = self.v[self.curRow][self.pos]
        self.pos += 1
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        # Reset the pointers to the next feasible location
        while self.curRow < len(self.v) and self.pos == len(self.v[self.curRow]):
            self.curRow += 1
            self.pos = 0
        return self.curRow < len(self.v)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
