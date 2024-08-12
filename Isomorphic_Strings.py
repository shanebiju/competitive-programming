class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] not in dict1 and t[i] not in dict2:
                    dict1[s[i]] = t[i]
                    dict2[t[i]] = s[i]
                elif dict1.get(s[i]) != t[i] or dict2.get(t[i]) != s[i]:
                    return False
            return True
        else:
            return False

# Boilerplate code
if __name__ == "__main__":
    # Example usage
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")

    solution = Solution()
    result = solution.isIsomorphic(s, t)
    print("The strings are isomorphic:", result)
