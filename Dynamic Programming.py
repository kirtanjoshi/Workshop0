# Task 1

def min_coins(coins,amount):
 """
 Findstheminimumnumberofcoinsneededtomakeupagivenamountusingdynamic
 programming.
 Thisfunctionsolvesthecoinchangeproblembydeterminingthefewestnumberof
 coinsfromagivensetofcoindenominationsthatsumuptoatargetamount.The
 solutionusesdynamicprogramming(tabulation)toiterativelybuilduptheminimum
 numberofcoinsrequiredfor eachamount.
 Parameters:
 coins(listofint):Alistof coindenominationsavailableformakingchange.Each
 coin denominationisapositiveinteger.
 amount (int):Thetargetamountforwhichweneedtofindtheminimumnumberofcoins
 .It mustbeanon-negativeinteger.
 Returns:
 int:The minimumnumberofcoins requiredtomakethegivenamount.
 Ifitisnotpossibletomaketheamountwiththegivencoins,returns-1.
 Example:
 >>>min_coins([1,2,5],11)
 3
 >>>min_coins([2],3)-1
 """
 dp=[float("inf")]*(amount+1)
 dp[0]=0
 for coin in coins:
    for i in range(coin,amount+1):
        dp[i]=min(dp[i],dp[i-coin]+1)
 return dp[amount]if dp[amount]!=float("inf") else -1


# Test cases
print(min_coins([1, 2, 5], 11))  



# Task 2
def longest_common_subsequence(s1, s2):
    """
    Finds the length of the longest common subsequence (LCS) between two strings using dynamic programming.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        int: The length of the longest common subsequence.

    Example:
        >>> longest_common_subsequence("abcde", "ace")
        3
        >>> longest_common_subsequence("abc", "def")
        0
    """
    # Initialize a 2D DP table with 0s, where dp[i][j] represents the LCS of s1[0...i-1] and s2[0...j-1]
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]: 
                dp[i][j] = dp[i - 1][j - 1] + 1
            else: 
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(s1)][len(s2)]

# Test cases
print(longest_common_subsequence("abcde", "ace")) 
print(longest_common_subsequence("abc", "def"))   

#Task 3
def knapsack(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming to maximize the value
    of items that can be carried without exceeding the weight capacity.

    Args:
        weights (list of int): A list representing the weights of items.
        values (list of int): A list representing the values of items.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        int: The maximum value that can be achieved within the given weight capacity.

    Example:
        >>> knapsack([1, 2, 3], [10, 20, 30], 5)
        50
    """
    n = len(weights)  # Number of items
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):  # Loop through each item
        for w in range(1, capacity + 1):  # Loop through each weight capacity
            if weights[i - 1] <= w:  # If the item can fit into the current capacity
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]  # If the item can't fit, take the previous value

    # The maximum value will be in dp[n][capacity]
    return dp[n][capacity]

# Test the function
weights = [1, 3, 4, 5]
values =[1, 4, 5, 7]
capacity = 7
print(knapsack(weights, values, capacity))

