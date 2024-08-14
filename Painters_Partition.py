class Solution:
    def minTime(self, arr, n, k):
        # Your logic here
        l = max(arr)
        h = sum(arr)
        ans = 0
        
        while l <= h:
            mid = (l + h) // 2
            painter = 1
            total_boards = 0
            
            for x in arr:
                if total_boards + x <= mid:
                    total_boards += x
                else:
                    painter += 1
                    total_boards = x
            
            if painter > k:
                l = mid + 1
            else:
                ans = mid
                h = mid - 1
        
        return ans


# Boilerplate code for reading input and running the solution
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    
    solution = Solution()
    result = solution.minTime(arr, n, k)
    print(result)
