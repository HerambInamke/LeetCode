class Solution {
    public boolean checkDivisibility(int n) {
        // Store the original value of n, as n will be modified during digit extraction.
        int originalN = n; 

        int sumOfDigits = 0;
        int productOfDigits = 1;

        // Use a temporary variable to extract digits
        int tempN = n; 
        while (tempN > 0) {
            int digit = tempN % 10; // Get the last digit
            sumOfDigits += digit;   // Add to sum
            productOfDigits *= digit; // Multiply to product
            tempN /= 10;            // Remove the last digit
        }

        // Calculate the combined sum of digit sum and digit product
        int combinedSum = sumOfDigits + productOfDigits;

        // Check if the original number is divisible by the combined sum.
        // combinedSum will always be positive for a positive 'n', so no division by zero issue.
        return originalN % combinedSum == 0;
    }
}