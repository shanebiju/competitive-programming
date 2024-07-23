from typing import List, Tuple

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = len(nums) - 1
        l = 0
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return -1

if __name__ == "__main__":
    # Prompt the user for input
    nums_input = input("Enter a sorted list of integers (comma-separated): ")
    target_input = input("Enter the target integer: ")

    try:
        # Parse the input into a list of integers
        nums = list(map(int, nums_input.split(',')))

        # Parse the target into an integer
        target = int(target_input)

        # Create an instance of Solution
        solution = Solution()

        # Perform the search
        result = solution.search(nums, target)

        # Display the result
        if result != -1:
            print(f"The target {target} is at index {result} in the list.")
        else:
            print(f"The target {target} is not in the list.")
    except ValueError:
        print("Invalid input! Please enter valid integers.")
