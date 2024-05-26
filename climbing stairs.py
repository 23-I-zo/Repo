class Solution(object):
    def climbStairs(self, n):
        memo = {}  # Dictionary for memoization

        # Wrapper function to handle memoization
        return self.ways(n, memo)

    def ways(self, n, memo):
        if n in memo:
            return memo[n]

        # Base cases
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Recursive case: Calculate ways for n using memoization
        memo[n] = self.ways(n - 1, memo) + self.ways(n - 2, memo)
        return memo[n]

# Example usage:
# Instantiate the Solution class
sol = Solution()
# Call the climbStairs method to find the number of ways to climb 'n' stairs
print(sol.climbStairs(5))  # Output will be the number of ways to climb 5 stairs
