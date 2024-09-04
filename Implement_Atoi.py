class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        numberReached = False
        ans = 0
        sign = float('-inf')
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        for x in s:
            if not numberReached and (x == '+' or x == '-') and sign == float('-inf'):
                sign = -1 if x == '-' else 1
            elif ord(x) >= 48 and ord(x) <= 57:
                numberReached = True
                ans = ans * 10 + int(x)
            else:
                break
        if sign == float('-inf'):
            sign = 1
        if sign * ans < INT_MIN:
            return INT_MIN
        if sign * ans > INT_MAX:
            return INT_MAX
        return sign * ans

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    solution = Solution()
    result = solution.myAtoi(user_input)
    print("Converted integer:", result)
