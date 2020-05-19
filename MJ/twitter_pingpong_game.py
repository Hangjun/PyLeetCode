# Suppose two players A and B play ping pong. The first player to get to 11 points wins the match. The players alternate after every 2nd serve (e.g. player A serves twice first, then player B serves twice and so on). 
# If A is serving, the probability of A winning the point is pA.
# If B is serving, the probability of B winning the point is pB.
# Note: A player can win a point, even when they are not serving. e.g. 
# If A is serving, the probability of B winning the point is (1 - pA).

# If player A serves first, what is the probability of player A winning the match?

# A,A,B,B,A,A,B,B,A,A,B....

# pA -> 1:0; (1-pA): 0:1
# pA * pA -> 2:0; pA * (1-pA): 1:1; (1-pA)^2 -> 0:2

# pA * pA * pB -> 2:1, pA * pA * (1-pBb) -> 3:0
# pA * (1-pA) * pB -> 1:2, pA * (1-pA) * (1-pB) -> 2:1
# (1-pA) * (1-pA) * pB -> 0:3, (1-pA) * (1-pA) * (1-pB) -> 1:2

# pA * (1-pA) * pB + (1-pA) * (1-pA) * (1-pB) = P(1:2)

# dp[i][j] := prob of score i:j after (i+j) rounds of serving
# dp[i][j] <- dp[i-1][j] or dp[i][j-1]
# sum(dp[11][<11]) = total prob of A winning the match
# (i+j) = 1,2 -> A
#  3,4 -> B

# What are the probibilities that A wins at move X and B wins at move X?


def winningProb(pA, pB, totalPoints):
    # dp[i][j] = prob of i:j
    dp = [[0 for _ in range(totalPoints+1)] for _ in range(totalPoints+1)]
    # initialization
    dp[0][0] = 1
    # initialize first row: dp[0][j]
    for j in range(1, totalPoints+1):
        if j % 4 in (1, 2):
            dp[0][j] = dp[0][j-1] * (1-pA)
        else:
            dp[0][j] = dp[0][j-1] * pB
            
    for i in range(1, totalPoints+1):
        if i % 4 in (1, 2):
            dp[i][0] = dp[i-1][0] * pA
        else:
            dp[i][0] = dp[i-1][0] * (1-pB)
    
    for i in range(1, totalPoints+1):
        for j in range(1, totalPoints+1):
            if (i+j) % 4 in (1, 2):
                if i == totalPoints:
                    dp[i][j] = dp[i-1][j] * pA
                else:
                    dp[i][j] = dp[i-1][j] * pA + dp[i][j-1] * (1 - pA)
            else:
                dp[i][j] = dp[i-1][j] * (1 - pB) + dp[i][j-1] * pB
    print dp
    
    return sum(dp[totalPoints-1][i] for i in range(totalPoints)) 
