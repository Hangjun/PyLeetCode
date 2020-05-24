"""
On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.

A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions.

The CPU is single threaded which means that only one function is being executed at a given time unit.

Return the exclusive time of each function, sorted by their function id.

 

Example 1:



Input:
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3, 4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing for 1 unit of time. 
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
 

Note:

1 <= n <= 100
Two functions won't start or end at the same time.
Functions will always log when they exit.
"""

# Stack. Time: O(n), Space: O(n). The caveat is that, when a function ends, we need to increment the time counter by 1 to correctly
# account for the previously halted function.
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # res[i] = accumulated execution cycles of function i
        res = [0 for _ in range(n)]
        stack = []
        prev_time = 0
        for log in logs:
            function_id, exe_type, time = log.split(":")
            function_id = int(function_id)
            time = int(time)
            
            if exe_type == "start":
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(function_id)
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return res
