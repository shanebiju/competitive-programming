class Solution:
    def print2largest(self, arr):
        # Code Here
        if len(arr) == 1:
            return -1
        maxi = max(arr)
        prevmax = float('-inf')
        for x in arr:
            if x > prevmax and x != maxi:
                prevmax = x
        ans = -1 if prevmax == float('-inf') else prevmax
        return ans

# Boilerplate code starts here

if __name__ == "__main__":
    # Input prompt for the array
    arr = list(map(int, input("Enter the array elements separated by space: ").strip().split()))

    # Create an instance of Solution
    sol = Solution()

    # Call the print2largest method
    result = sol.print2largest(arr)

    # Print the result
    print(f"The second largest element is: {result}")
