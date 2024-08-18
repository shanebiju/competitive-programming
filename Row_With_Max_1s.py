class Solution:
    def rowWithMax1s(self, arr):
        # Your logic here
        m = len(arr)
        n = len(arr[0])
        maxi = float('-inf')
        return_idx = -1

        def findFirstOccurence(a, n):
            l = 1
            h = n - 1
            idx = float('+inf')
            while l <= h:
                mid = (l + h) // 2
                if a[mid] == 1:
                    idx = min(idx, mid)
                    h = mid - 1
                else:
                    l = mid + 1
            if idx != float('+inf'):
                return idx
            else:
                return -1

        for i in range(0, m):
            if arr[i][0] == 1:
                return i
            else:
                num = findFirstOccurence(arr[i], n)
                if maxi < n - num and num != -1:
                    maxi = max(maxi, n - num)
                    return_idx = i
        return return_idx


def main():
    # Taking input from the user
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    
    # Initializing the matrix
    matrix = []
    print("Enter the binary matrix row by row:")
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Creating an object of the Solution class
    sol = Solution()
    
    # Calling the rowWithMax1s function
    result = sol.rowWithMax1s(matrix)
    
    # Printing the result
    print("The row with the maximum number of 1s is:", result)

if __name__ == "__main__":
    main()
