class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for x in s:
            if x not in dict1:
                dict1[x] = 1
            else:
                dict1[x] += 1
        for x in t:
            if x not in dict2:
                dict2[x] = 1
            else:
                dict2[x] += 1
        return dict1 == dict2

if __name__ == "__main__":
    # Read input from user
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")

    # Create an instance of the Solution class
    sol = Solution()

    # Get the result from the isAnagram method
    result = sol.isAnagram(s, t)

    # Print the result
    print(f"The strings '{s}' and '{t}' are anagrams: {result}")
