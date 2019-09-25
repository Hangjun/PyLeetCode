"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""

# This is almost the same as https://leetcode.com/problems/design-hashmap/. We implement the hash set using chaining. All operations
 are O(1) on average.

class ListNode(object):
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 997
        self.ht = [None] * self.m

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket_idx = key % self.m
        if self.ht[bucket_idx] == None:
            self.ht[bucket_idx] = ListNode(key)
            return
        # traverse the list to see if node with key already exists
        cur = self.ht[bucket_idx]
        while True:
            if cur.key == key: # key already exsits, return
                return
            if cur.next == None:
                break
            cur = cur.next
        # the bucket exists but this key has not appeared in this bucket's chained list
        cur.next = ListNode(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket_idx = key % self.m
        if self.ht[bucket_idx] == None:
            return
        # traverse the list to find the key to remove
        cur = self.ht[bucket_idx]
        if cur.key == key:
            self.ht[bucket_idx] = cur.next
            return
        pre = cur
        cur = cur.next
        while cur and cur.key != key:
            cur, pre = cur.next, pre.next
        if not cur:
            return
        pre.next = cur.next

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucket_idx = key % self.m
        cur = self.ht[bucket_idx]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
