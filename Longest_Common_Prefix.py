from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        length = len(strs[0])
        totalLength = len(strs)
        pos = length
        for i in range(0, length):
            if strs[0][i] != strs[totalLength - 1][i]:
                pos = i
                break
        return strs[0][0:pos]

if __name__ == "__main__":
    # Read input from user
    strs = input("Enter a list of strings separated by space: ").split()

    # Create an instance of the Solution class
    sol = Solution()

    # Get the result from the longestCommonPrefix method
    result = sol.longestCommonPrefix(strs)

    # Print the result
    print(f"The longest common prefix is: '{result}'")
