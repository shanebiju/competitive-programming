class Solution:
    def solve(self, n, k, stalls):
        stalls.sort()
        l = 1
        h = stalls[n - 1] - stalls[0]
        maxi = float('-inf')
        while l <= h:
            mid = (l + h) // 2
            cows = 1
            prev_pos = 0
            i = 1
            while i < n:
                if stalls[i] - stalls[prev_pos] >= mid:
                    cows = cows + 1
                    prev_pos = i
                if cows == k:
                    break
                i = i + 1
            if cows == k:
                maxi = max(maxi, mid)
                l = mid + 1
            else:
                h = mid - 1
        return maxi

if __name__ == '__main__':
    # Read input values
    n = int(input("Enter the number of stalls: "))
    k = int(input("Enter the number of cows: "))
    stalls = list(map(int, input("Enter the positions of the stalls separated by spaces: ").split()))

    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the solve method and print the result
    result = solution.solve(n, k, stalls)
    print("The largest minimum distance is:", result)
