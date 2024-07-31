from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        l = min(bloomDay)
        h = max(bloomDay)
        mini = max(bloomDay)
        while l <= h:
            mid = (l + h) // 2
            adj_cnt = 0
            bouquet = 0
            for x in bloomDay:
                if x <= mid:
                    adj_cnt += 1
                else:
                    bouquet += (adj_cnt // k)
                    adj_cnt = 0
            if adj_cnt != 0:
                bouquet += (adj_cnt // k)
            if bouquet >= m:
                mini = min(mini, mid)
                h = mid - 1
            else:
                l = mid + 1
        return mini

if __name__ == "__main__":
    # Get input from the user
    try:
        # Input: bloomDay list
        bloomDay_input = input("Enter the bloom days (separated by spaces): ")
        bloomDay = list(map(int, bloomDay_input.split()))

        # Input: number of bouquets needed
        m = int(input("Enter the number of bouquets needed: "))

        # Input: number of adjacent flowers needed for a bouquet
        k = int(input("Enter the number of adjacent flowers needed for each bouquet: "))

        # Create an instance of Solution
        solution = Solution()

        # Calculate the minimum number of days
        result = solution.minDays(bloomDay, m, k)

        # Display the result
        if result != -1:
            print(f"Minimum number of days required: {result}")
        else:
            print("It is not possible to make the required bouquets.")

    except ValueError:
        print("Invalid input! Please enter valid integers.")
