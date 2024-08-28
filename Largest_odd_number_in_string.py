class Solution:
    def largestOddNumber(self, nums: str) -> str:
        length = len(nums)
        for i in range(length - 1, -1, -1):
            if nums[i] in "13579":
                return nums[0:i + 1]
        return ""

if __name__ == "__main__":
    nums = input("Enter a string of digits: ")
    sol = Solution()
    result = sol.largestOddNumber(nums)
    print(f"The largest odd number is: '{result}'")
