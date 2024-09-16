from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def LTE(arr, target):
            if target == -1:
                return 0
            l, r = 0, 0
            length = len(arr)
            oddFreq = 0
            subarrCount = 0
            while r < length:
                if arr[r] % 2 == 1:
                    oddFreq += 1
                while oddFreq > target:
                    if arr[l] % 2 == 1:
                        oddFreq -= 1
                    l += 1
                subarrCount += (r - l + 1)
                r += 1
            return subarrCount
        
        return LTE(nums, k) - LTE(nums, k - 1)

if __name__ == "__main__":
    # Read input from user
    nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    k = int(input("Enter the value of k: "))

    # Create an instance of the solution class
    obj = Solution()

    # Call the function with the input values
    result = obj.numberOfSubarrays(nums, k)

    # Print the result
    print(result)
