from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        l = 0
        h = len(arr) - 1
        while l <= h:
            mid = (l + h) // 2
            if arr[mid] - mid - 1 < k:
                l = mid + 1
            else:
                h = mid - 1
        return arr[h] + (k - (arr[h] - h - 1))

if __name__ == '__main__':
    # Example inputs
    arr = list(map(int, input("Enter the sorted array of integers separated by space: ").split()))
    k = int(input("Enter the value of k: "))
    
    solution = Solution()
    result = solution.findKthPositive(arr, k)
    print(f"The {k}-th missing positive number is: {result}")
