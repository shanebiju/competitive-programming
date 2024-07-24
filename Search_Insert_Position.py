from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Implement the logic here
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                h=mid-1
            else:
                l=mid+1
        return l

if __name__ == "__main__":
    try:
        # Get input from the user
        nums_input = input("Enter a sorted list of integers (comma-separated): ")
        target_input = input("Enter the target integer to search/insert: ")

        # Parse the inputs
        nums = list(map(int, nums_input.split(',')))
        target = int(target_input)

        # Create an instance of Solution
        solution = Solution()

        # Find the insert position of the target in the array
        result = solution.searchInsert(nums, target)

        # Display the result
        print(f"The target {target} should be at index {result}.")

    except ValueError:
        print("Invalid input! Please enter valid integers.")
