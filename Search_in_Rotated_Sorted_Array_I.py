from typing import List

class Solution:
    def search(self, a: List[int], target: int) -> int:
        # Implement the logic here
        l=0
        h=len(a)-1
        while l<=h:
            mid=(l+h)//2
            if a[mid]==target:
                return mid
            if a[mid]>=a[l]:
                if a[l]<=target<a[mid]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if a[mid]<target<=a[h]:
                    l=mid+1
                else:
                    h=mid-1
        return -1

if __name__ == "__main__":
    try:
        # Get input from the user
        arr_input = input("Enter a rotated sorted list of integers (comma-separated): ")
        target_input = input("Enter the target integer to search for: ")

        # Parse the inputs
        a = list(map(int, arr_input.split(',')))
        target = int(target_input)

        # Create an instance of Solution
        solution = Solution()

        # Find the index of the target in the rotated sorted array
        result = solution.search(a, target)

        # Display the result
        if result != -1:
            print(f"The target {target} is at index {result}.")
        else:
            print(f"The target {target} is not in the list.")

    except ValueError:
        print("Invalid input! Please enter valid integers.")
