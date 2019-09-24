"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""

# Chaining. put: O(1), get: O(1), remove: O(1) on average.
class ListNode:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None
        
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 997
        self.ht = [None] * self.m

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        bucket_idx = key % self.m
        if self.ht[bucket_idx] == None:
            self.ht[bucket_idx] = ListNode(key, value)
            return
        p = self.ht[bucket_idx]
        while True:
            if p.pair[0] == key:
                p.pair = (key, value)
                return
            if p.next == None: break
            p = p.next
        p.next = ListNode(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket_idx = key % self.m
        if self.ht[bucket_idx] == None:
            return -1
        p = self.ht[bucket_idx]
        while p:
            if p.pair[0] == key:
                return p.pair[1]
            p = p.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        bucket_idx = key % self.m
        if self.ht[bucket_idx] == None:
            return
        cur = self.ht[bucket_idx]
        # if we are removing the first node, simply remove it
        if cur.pair[0] == key:
            self.ht[bucket_idx] = cur.next
            return
        pre = self.ht[bucket_idx]
        cur = cur.next
        while cur and cur.pair[0] != key:
            cur = cur.next
            pre = pre.next
        if not cur:
            return
        pre.next = cur.next
            

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
