class Solution:
    def reverseWords(self, s: str) -> str:
        # Your logic
        s = s.strip()
        l = len(s) - 1
        ans = ""
        word = ""
        i = l
        while i >= 0:
            if s[i] != ' ':
                word = s[i] + word
            else:
                if i + 1 != l + 1 and s[i + 1] != ' ':
                    ans = ans + word + " "
                    word = ""
            i = i - 1
        return ans + word


# Boilerplate code
if __name__ == "__main__":
    solution = Solution()
    input_str = input("Enter the string: ")
    result = solution.reverseWords(input_str)
    print("Reversed words:", result)
