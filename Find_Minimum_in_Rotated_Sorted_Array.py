from typing import List

class Solution:
    def findMin(self, a: List[int]) -> int:
        # Implement the logic here
        l=0
        h=len(a)-1
        mini=float('inf')
        while l<=h:
            mid=(l+h)//2
            if a[mid]>a[l]:
                mini=min(a[l],mini)
                l=mid+1
            elif a[mid]<a[l]:
                mini=min(mini,a[mid])
                h=mid-1
            else:
                mini=min(mini,a[l])
                l=l+1
        return mini


if __name__ == "__main__":
    try:
        # Get input from the user
        arr_input = input("Enter a list of integers representing a rotated sorted array (comma-separated): ")

        # Parse the input
        a = list(map(int, arr_input.split(',')))

        # Create an instance of Solution
        solution = Solution()

        # Find the minimum element in the array
        result = solution.findMin(a)

        # Display the result
        print(f"The minimum element in the rotated sorted array is: {result}")

    except ValueError:
        print("Invalid input! Please enter valid integers.")
