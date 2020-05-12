"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
 
 

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
"""

"""
This problem is almost exactly the same as Problem 253. Meeting Rooms II. We use the ordered map solution here as well. The 
idea is similarly to record the passenger count at each timestamp. Then we sort the timestamp and replay the passenger count 
along the time.

Time: O(nlogn), Space: O(n).
"""
from collections import defaultdict
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        passengerCount = defaultdict(int)
        for n, on, off in trips:
            passengerCount[on] += n
            passengerCount[off] -= n
        for _, count in sorted(passengerCount.items(), key=lambda kv: (kv[0], kv[1])):
            capacity -= count
            if capacity < 0:
                return False
        return True
        
# This problem also specifies that there cannot be more than 1000 stops. We can then use a fixed length array to record passenger 
# count at each stop sequentially, thus avoids the need to sort.
# Time: O(n), Space: O(1).
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        passengerCount = [0 for _ in range(1001)]
        for n, on, off in trips:
            passengerCount[on] += n
            passengerCount[off] -= n
        for count in passengerCount:
            capacity -= count
            if capacity < 0:
                return False
        return True
