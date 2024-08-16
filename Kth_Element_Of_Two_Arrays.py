class Solution:
    def kthElement(self, k, arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        if m > n:
            return self.kthElement(k, arr2, arr1)
        l = max(0, k - n)
        h = min(k, m)
        while l <= h:
            mid1 = (l + h) // 2
            mid2 = k - mid1
            l1 = float('-inf') if mid1 == 0 else arr1[mid1 - 1]
            r1 = float('+inf') if mid1 == m else arr1[mid1]
            l2 = float('-inf') if mid2 == 0 else arr2[mid2 - 1]
            r2 = float('+inf') if mid2 == n else arr2[mid2]
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                h = mid1 - 1
            else:
                l = mid1 + 1
        return -1

# Boilerplate code starts here

if __name__ == "__main__":
    k = int(input("Enter the value of k: "))

    arr1 = list(map(int, input("Enter the first sorted array: ").strip().split()))

    arr2 = list(map(int, input("Enter the second sorted array: ").strip().split()))

    sol = Solution()

    result = sol.kthElement(k, arr1, arr2)

    print(f"The {k}th smallest element is: {result}")
