class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def LTE(nums, k):
            if k == -1:
                return 0
            mydict = {}
            dictlen = 0
            l, r = 0, 0
            count = 0
            length = len(nums)

            while r < length:
                if nums[r] not in mydict:
                    mydict[nums[r]] = 1
                    dictlen += 1
                else:
                    mydict[nums[r]] += 1

                while dictlen > k:
                    mydict[nums[l]] -= 1
                    if mydict[nums[l]] == 0:
                        mydict.pop(nums[l])
                        dictlen -= 1
                    l += 1

                count += (r - l + 1)
                r += 1
            return count

        return LTE(nums, k) - LTE(nums, k - 1)


if __name__ == "__main__":
    nums = list(map(int, input("Enter the array of numbers: ").split()))
    k = int(input("Enter the value of k: "))
    solution = Solution()
    result = solution.subarraysWithKDistinct(nums, k)
    print(f"Number of subarrays with exactly {k} distinct elements: {result}")
