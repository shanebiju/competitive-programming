from typing import List

class Solution:
    def findPages(self, n: int, arr: List[int], m: int) -> int:
        if m > n:
            return -1
        h = sum(arr)
        l = max(arr)
        while l <= h:
            mid = (l + h) // 2
            stu = 1
            maxi = 0
            for x in arr:
                if maxi + x <= mid:
                    maxi += x
                else:
                    stu += 1
                    maxi = x
            if stu > m:
                l = mid + 1
            else:
                ans = mid
                h = mid - 1
        return ans

if __name__ == "__main__":
    n = int(input("Enter the number of books: "))
    arr = list(map(int, input(f"Enter the number of pages in each of the {n} books, separated by space: ").split()))
    m = int(input("Enter the number of students: "))
    
    sol = Solution()
    result = sol.findPages(n, arr, m)
    print(result)
