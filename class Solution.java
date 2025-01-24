class Solution {
public static void main(String[] args) {
    public int climbStairs(int n) {
        if (n == 1) return 1; // Base case: only one step
        
        int first = 1; // dp[1]
        int second = 2; // dp[2]
        
        // Compute from 3 to n
        for (int i = 3; i <= n; i++) {
            int current = first + second; // dp[n] = dp[n-1] + dp[n-2]
            first = second; // Update first to be the previous second
            second = current; // Update second to be the current
        }
        
        return n == 2 ? second : first; // Return result for n
    }
}
}
