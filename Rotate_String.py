class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = s + s
        if goal in s:
            return True
        return False

if __name__ == "__main__":
    # Read input from user
    s = input("Enter the string s: ")
    goal = input("Enter the string goal: ")

    # Create an instance of the Solution class
    sol = Solution()

    # Get the result from the rotateString method
    result = sol.rotateString(s, goal)

    # Print the result
    print(f"The string '{goal}' can be obtained by rotating '{s}': {result}")
