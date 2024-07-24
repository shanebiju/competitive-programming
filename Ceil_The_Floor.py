from typing import List

class Solution:
    def getFloorAndCeil(self, x: int, arr: List[int]) -> List[int]:
        floor=float('-inf');ceil=float('+inf')
        for num in arr:
            if num>=x and num<ceil:
                ceil=min(ceil,num)
            if num<=x and num>floor:
                floor=max(floor,num)
        if floor==float('-inf') and ceil==float('+inf'):
            return [-1,-1]
        elif floor==float('-inf'):
            return [-1,ceil]
        elif ceil==float('+inf'):
            return [floor,-1]
        else:
            return [floor,ceil]

if __name__ == "__main__":
    # Example input
    try:
        # Get input from the user
        arr_input = input("Enter a list of integers (comma-separated): ")
        target_input = input("Enter the target integer to find floor and ceil: ")

        # Parse the inputs
        arr = list(map(int, arr_input.split(',')))
        x = int(target_input)

        # Create an instance of Solution
        solution = Solution()

        # Find the floor and ceil of the target in the array
        result = solution.getFloorAndCeil(x, arr)

        # Display the result
        print(f"The floor and ceil of {x} in the list are: {result}")

    except ValueError:
        print("Invalid input! Please enter valid integers.")
