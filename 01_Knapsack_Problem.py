# Time Complexity :
- O(2^n), where n is the number of items due to recursion exploring all subsets

# Space Complexity :
- O(n), for the recursion call stack

# Did this code successfully run on Leetcode: No (GeeksforGeeks)

# Any problem you faced while coding this : No

# Returns the maximum value that can be put in a knapsack of capacity W
def knapsackRec(W, val, wt, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    pick = 0

    # Pick nth item if it does not exceed the capacity of knapsack
    if wt[n - 1] <= W:
        pick = val[n - 1] + knapsackRec(W - wt[n - 1], val, wt, n - 1)

    # Don't pick the nth item
    notPick = knapsackRec(W, val, wt, n - 1)
    
    return max(pick, notPick)

def knapsack(W, val, wt):
    n = len(val)
    return knapsackRec(W, val, wt, n)

# Example usage
if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4
    print(knapsack(W, val, wt))
