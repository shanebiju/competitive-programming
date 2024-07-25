# User function Template for python3
from typing import List

class Solution:
    def count(self, a: List[int], n: int, target: int) -> int:
        # Implement the logic here
        l=0
        h=len(a)-1
        first=float('inf');last=float('-inf')
        while l<=h:
            mid=(l+h)//2
            if a[mid]==target:
                first=min(first,mid)
                h=mid-1
            elif a[mid]<target:
                l=mid+1
            else:
                h=mid-1
        if first==float('inf'):
            return 0
        l=0
        h=len(a)-1
        while l<=h:
            mid=(l+h)//2
            if a[mid]==target:
                last=max(last,mid)
                l=mid+1
            elif a[mid]<target:
                l=mid+1
            else:
                h=mid-1
        return last-first+1

if __name__ == "__main__":
    try:
        # Get input from the user
        arr_input = input("Enter a list of integers (comma-separated): ")
        target_input = input("Enter the integer to count occurrences of: ")

        # Parse the inputs
        a = list(map(int, arr_input.split(',')))
        x = int(target_input)
        n = len(a)

        # Create an instance of Solution
        solution = Solution()

        # Find the number of occurrences of x in the array
        result = solution.count(a, n, x)

        # Display the result
        print(f"The number {x} occurs {result} times in the list.")

    except ValueError:
        print("Invalid input! Please enter valid integers.")
