from typing import List

class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        l = 0
        h = len(a) - 1
        length = len(a) - 1
        if length == 0:
            return 0
        while l <= h:
            mid = (l + h) // 2
            if mid == 0:
                if a[mid] > a[mid + 1]:
                    return mid
            if mid == length:
                if a[mid] > a[mid - 1]:
                    return mid
            if a[mid - 1] < a[mid] > a[mid + 1]:
                return mid
            if a[mid] < a[mid + 1]:
                l = mid + 1
            else:
                h = mid - 1

if __name__ == "__main__":
    try:
        # Get input from the user
        array_input = input("Enter a list of integers (comma-separated): ")

        # Parse the input
        a = list(map(int, array_input.split(',')))

        # Create an instance of the Solution class
        solution = Solution()

        # Call the findPeakElement function
        result = solution.findPeakElement(a)

        # Display the result
        print(f"The peak element is at index: {result}")

    except ValueError:
        print("Invalid input! Please enter a valid list of integers.")
