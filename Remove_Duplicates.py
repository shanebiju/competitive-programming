from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i, j = 0, 0
        if length == 1:
            return 1
        while j < length:
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1
        return i + 1

if __name__ == "__main__":
    # Input from the user
    nums = list(map(int, input("Enter the list of integers separated by space: ").split()))
    
    # Creating an instance of the Solution class
    obj = Solution()
    
    # Calling the removeDuplicates method and printing the result
    result = obj.removeDuplicates(nums)
    print("The number of unique elements is:", result)
    print("Modified list with unique elements:", nums[:result])
