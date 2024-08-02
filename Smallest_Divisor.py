import math
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], k: int) -> int:
        l = 1
        h = max(nums)
        mini = sum(nums)

        while l <= h:
            mid = (l + h) // 2
            s = 0

            for x in nums:
                s += math.ceil(x / mid)

            if s > k:
                l = mid + 1
            else:
                mini = min(mini, mid)
                h = mid - 1

        return mini

if __name__ == "__main__":
    nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    k = int(input("Enter the value of k: "))

    solution = Solution()
    result = solution.smallestDivisor(nums, k)

    print(f"The smallest divisor is: {result}")
