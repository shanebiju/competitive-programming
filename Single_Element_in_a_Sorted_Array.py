from typing import List

class Solution:
    def singleNonDuplicate(self, a: List[int]) -> int:
        # Logic to be implemented here
        l=0
        h=len(a)-1
        if len(a)==1:
            return a[0]
        length=len(a)
        while l<=h:
            mid=(l+h)//2
            if mid==0:
                if a[mid]!=a[mid+1]:
                    return a[mid]
            if mid==length-1:
                if a[mid]!=a[mid-1]:
                    return a[mid]
            if a[mid-1]!=a[mid] and a[mid+1]!=a[mid]:
                return a[mid]
            if mid+1!=length and mid%2==0 and a[mid]==a[mid+1] or mid!=0 and mid%2==1 and a[mid]==a[mid-1]:
                l=mid+1
            else:
                h=mid-1

if __name__ == "__main__":
    try:
        # Get input from the user
        array_input = input("Enter a sorted list of integers (comma-separated): ")

        # Parse the input
        a = list(map(int, array_input.split(',')))

        # Create an instance of the Solution class
        solution = Solution()

        # Call the singleNonDuplicate function
        result = solution.singleNonDuplicate(a)

        # Display the result
        print(f"The single non-duplicate element is: {result}")

    except ValueError:
        print("Invalid input! Please enter a valid list of integers.")
