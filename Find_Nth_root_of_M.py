class Solution:
    def NthRoot(self, n, m):
        l = 0
        h = m // n
        if m == 1:
            return 1
        while l <= h:
            mid = (l + h) // 2
            nth = mid ** n
            if nth == m:
                return mid
            if nth < m:
                l = mid + 1
            else:
                h = mid - 1
        return -1

if __name__ == "__main__":
    try:
        # Get input from the user
        n_input = input("Enter the value of n (root degree): ")
        m_input = input("Enter the value of m (number to find the root of): ")

        # Parse the input
        n = int(n_input)
        m = int(m_input)

        # Create an instance of the Solution class
        solution = Solution()

        # Call the NthRoot function
        result = solution.NthRoot(n, m)

        # Display the result
        if result != -1:
            print(f"The {n}th root of {m} is: {result}")
        else:
            print(f"The {n}th root of {m} is not an integer.")

    except ValueError:
        print("Invalid input! Please enter valid integers for n and m.")
