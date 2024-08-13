from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        h = sum(nums)
        while l <= h:
            mid = (l + h) // 2
            sub_arr = 1
            sub_arr_sum = 0
            for x in nums:
                if x + sub_arr_sum <= mid:
                    sub_arr_sum = sub_arr_sum + x
                else:
                    sub_arr += 1
                    sub_arr_sum = x
            if sub_arr > k:
                l = mid + 1
            else:
                ans = mid
                h = mid - 1
        return ans

# Input handling
if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    nums = list(map(int, input("Enter the array elements separated by spaces: ").strip().split()))
    k = int(input("Enter the value of k: "))

    solution = Solution()
    result = solution.splitArray(nums, k)
    print(f"The minimum largest sum is: {result}")
