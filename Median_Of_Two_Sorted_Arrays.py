class Solution:
    def MedianOfArrays(self, array1, array2):
        n1 = len(array1)
        n2 = len(array2)

        if n1 > n2:
            return self.MedianOfArrays(array2, array1)

        l = 0
        r = n1
        left = (n1 + n2 + 1) // 2
        n = n1 + n2

        while l <= r:
            mid1 = (l + r) // 2
            mid2 = left - mid1

            l1 = float('-inf') if mid1 == 0 else array1[mid1 - 1]
            l2 = float('-inf') if mid2 == 0 else array2[mid2 - 1]
            r1 = float('inf') if mid1 == n1 else array1[mid1]
            r2 = float('inf') if mid2 == n2 else array2[mid2]

            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)

                median = (max(l1, l2) + min(r1, r2)) / 2

                if median == int(median):
                    return int(median)
                return median

            elif l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1

        return 0


if __name__ == "__main__":
    # Input: two arrays
    array1 = list(map(int, input("Enter the elements of array1 (space-separated): ").split()))
    array2 = list(map(int, input("Enter the elements of array2 (space-separated): ").split()))
    
    # Create an object of the Solution class
    sol = Solution()
    
    # Function call and print the result
    print("The median of the arrays is:", sol.MedianOfArrays(array1, array2))
