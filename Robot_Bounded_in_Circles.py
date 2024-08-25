class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        x, y = 0, 0
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in instructions:
            if i == 'G':
                x, y = x + move[direction][0], y + move[direction][1]
            elif i == 'R':
                direction = (direction + 1) % 4
            else:
                direction = 3 if direction == 0 else direction - 1
        if x == 0 and y == 0 or direction != 0:
            return True
        return False

if __name__ == "__main__":
    # Example usage:
    instructions = input("Enter robot instructions: ")
    solution = Solution()
    result = solution.isRobotBounded(instructions)
    print("Is the robot bounded in a circle?", result)
