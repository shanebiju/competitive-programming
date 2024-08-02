from typing import List

class Solution:
    def leastWeightCapacity(self, arr: List[int], n: int, d: int) -> int:
        l = max(arr)
        h = sum(arr)
        mini = sum(arr)

        while l <= h:
            mid = (l + h) // 2
            days = 1
            rem_weight = mid

            for x in arr:
                if x <= rem_weight:
                    rem_weight -= x
                else:
                    days += 1
                    rem_weight = mid - x

            if days > d:
                l = mid + 1
            else:
                mini = min(mid, mini)
                h = mid - 1

        return mini

if __name__ == "__main__":
    n = int(input("Enter the number of packages: "))
    arr = list(map(int, input(f"Enter the weights of the {n} packages separated by spaces: ").split()))
    d = int(input("Enter the number of days: "))

    solution = Solution()
    result = solution.leastWeightCapacity(arr, n, d)

    print(f"The least weight capacity needed to ship the packages within {d} days is: {result}")
