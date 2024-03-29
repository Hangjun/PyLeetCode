"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:




Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""

# Dynamic Programming. Time: O(n^2), Space: O(n).
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs = sorted(jobs, key=lambda x: (x[1], x[0], x[2]))
        dp = [0 for _ in range(n)] # dp[i] = max profit from jobs[0] to jobs[i] (might not be included)
        dp[0] = jobs[0][2]
        
        for i in range(1, n):
            curProfit = jobs[i][2]
            curMax = max(curProfit, dp[i-1]) # two choices: either include job i or not
            for j in range(i-1, -1, -1):
                if jobs[j][1] <= jobs[i][0]:
                    curMax = max(curMax, dp[j]+curProfit)
                    break
            dp[i] = curMax
        
        return dp[n-1]
        
# We can improve the time complexity to O(nlogn) if we use binary search to find the first previous job with endTime <= startTime of the current job.
