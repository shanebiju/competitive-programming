class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk = []
        ans = ''
        for x in s:
            if x == '(':
                if stk:
                    ans = ans + '('
                stk.append('(')
            else:
                a = stk.pop()
                if stk:
                    ans = ans + ')'
        return ans

# Boilerplate code to run the function
if __name__ == "__main__":
    # Example usage
    s = input("Enter the parentheses string: ")
    solution = Solution()
    result = solution.removeOuterParentheses(s)
    print(f"Result after removing outer parentheses: {result}")
