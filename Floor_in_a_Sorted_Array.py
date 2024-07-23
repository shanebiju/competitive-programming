from typing import List

class Solution:
    # User function Template for python3
    
    # Complete this function
    def findFloor(self, a: List[int], n: int, x: int) -> int:
        # Your code here
        l=0
        h=n-1
        if x<a[0]:
            return -1
        while l<=h:
            mid=(l+h)//2
            if a[mid]==x:
                return mid
            elif a[mid]<x:
                res=mid
                l=mid+1
            else:
                h=mid-1
        return res

if __name__ == "__main__":
    # Get input from the user
    a_input = input("Enter a sorted list of integers (comma-separated): ")
    n_input = input("Enter the number of elements in the list: ")
    x_input = input("Enter the target integer to find the floor: ")

    try:
        # Parse the inputs
        a = list(map(int, a_input.split(',')))
        n = int(n_input)
        x = int(x_input)

        # Create an instance of Solution
        solution = Solution()

        # Find the floor of x in the list a
        floor_index = solution.findFloor(a, n, x)

        # Display the result
        if floor_index != -1:
            print(f"The floor of {x} is at index {floor_index}, which is the element {a[floor_index]}.")
        else:
            print(f"There is no floor for {x} in the list.")
    except ValueError:
        print("Invalid input! Please enter valid integers.")
