class Solution:
    def floorSqrt(self, x):
        l = 0
        h = x // 2
        if x == 1:
            return 1
        while l <= h:
            mid = (l + h) // 2
            square = mid ** 2
            if square == x:
                return mid
            if square < x:
                l = mid + 1
            else:
                h = mid - 1
        return l - 1

if __name__ == "__main__":
    try:
        # Get input from the user
        x_input = input("Enter a non-negative integer to find its square root floor: ")

        # Parse the input
        x = int(x_input)

        # Create an instance of the Solution class
        solution = Solution()

        # Call the floorSqrt function
        result = solution.floorSqrt(x)

        # Display the result
        print(f"The floor of the square root of {x} is: {result}")

    except ValueError:
        print("Invalid input! Please enter a non-negative integer.")
