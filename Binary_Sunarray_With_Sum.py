class Solution:
    def numSubarraysWithSum(self, nums, goal):
        def LTE(arr, target):
            if target == -1:
                return 0
            subarrCount = 0
            l, r = 0, 0
            length = len(arr)
            oneFreq = 0
            while r < length:
                if arr[r] == 1:
                    oneFreq += 1
                while oneFreq > target:
                    if arr[l] == 1:
                        oneFreq -= 1
                    l += 1
                subarrCount += (r - l + 1)
                r += 1
            return subarrCount

        return LTE(nums, goal) - LTE(nums, goal - 1)


if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Size of the array
        nums = list(map(int, input().split()))  # Input array
        goal = int(input())  # Target sum
        obj = Solution()
        result = obj.numSubarraysWithSum(nums, goal)
        print(result)
