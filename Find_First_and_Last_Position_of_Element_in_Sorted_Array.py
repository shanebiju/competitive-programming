#Find_First_and_Last_Position_of_Element_in_Sorted_Array.py
from typing import List

class Solution:
    def searchRange(self, a: List[int], target: int) -> List[int]:
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
            return [-1,-1]
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
        return [first,last]

if __name__ == "__main__":
    try:
        # Get input from the user
        arr_input = input("Enter a list of integers (comma-separated): ")
        target_input = input("Enter the target integer to search for its range: ")

        # Parse the inputs
        a = list(map(int, arr_input.split(',')))
        target = int(target_input)

        # Create an instance of Solution
        solution = Solution()

        # Find the range of the target in the array
        result = solution.searchRange(a, target)

        # Display the result
        if result:
            print(f"The target {target} appears in the list at indices: {result}.")
        else:
            print(f"The target {target} does not appear in the list.")

    except ValueError:
        print("Invalid input! Please enter valid integers.")
