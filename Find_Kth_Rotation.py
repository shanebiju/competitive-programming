from typing import List

class Solution:
    def findKRotation(self, a: List[int]) -> int:
        # Implement the logic here
        l=0
        h=len(a)-1
        mid=(l+h)//2
        if a[l]<=a[mid]<=a[h]:
            return 0
        while l<=h:
            if l+1==h:
                return h
            mid=(l+h)//2
            if a[l]<a[mid]:
                l=mid
            else:
                h=mid

if __name__ == "__main__":
    try:
        # Get input from the user
        arr_input = input("Enter a list of integers representing a rotated sorted array (comma-separated): ")

        # Parse the input
        a = list(map(int, arr_input.split(',')))

        # Create an instance of Solution
        solution = Solution()

        # Find the number of rotations
        result = solution.findKRotation(a)

        # Display the result
        print(f"The array is rotated {result} times.")

    except ValueError:
        print("Invalid input! Please enter valid integers.")
