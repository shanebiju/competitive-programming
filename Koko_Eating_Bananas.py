from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mini = max(piles)
        while l <= r:
            mid = (l + r) // 2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / mid)
            if hrs > h:
                l = mid + 1
            else:
                mini = min(mini, mid)
                r = mid - 1
        return mini

if __name__ == "__main__":
    # User input handling
    try:
        # Input: list of piles
        piles_input = input("Enter the list of banana piles (separated by spaces): ")
        piles = list(map(int, piles_input.split()))

        # Input: number of hours
        h = int(input("Enter the number of hours: "))

        # Create an instance of Solution
        solution = Solution()

        # Calculate the minimum eating speed
        result = solution.minEatingSpeed(piles, h)

        # Display the result
        print(f"Minimum eating speed: {result}")

    except ValueError:
        print("Invalid input! Please enter valid integers.")
