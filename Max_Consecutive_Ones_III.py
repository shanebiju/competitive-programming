from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        mydict = {}
        length = len(nums)
        l, r = 0, 0
        maxLength = 0
        while r < length:
            if nums[r] not in mydict:
                mydict[nums[r]] = 1
            else:
                mydict[nums[r]] += 1
            if mydict.get(0, 0) <= k:
                maxLength = max(maxLength, r - l + 1)
            else:
                mydict[nums[l]] -= 1
                l += 1
            r += 1
        return maxLength

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    ob = Solution()
    print(ob.longestOnes(nums, k))
