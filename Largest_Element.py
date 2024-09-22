class Solution:
    def largest(self, arr: List[int]) -> int:
        largest = arr[0]
        length = len(arr)
        for i in range(1, length):
            if arr[i] > largest:
                largest = arr[i]
        return largest

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))

    sol = Solution()
    result = sol.largest(arr)
    print(f"The largest element in the array is: {result}")
