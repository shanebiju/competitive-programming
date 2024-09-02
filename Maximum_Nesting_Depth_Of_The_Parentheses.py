class Solution:
    def maxDepth(self, s: str) -> int:
        maxLen, stklen = 0, 0
        for x in s:
            if x == '(':
                stklen += 1
            elif x == ')':
                stklen -= 1
            maxLen = max(maxLen, stklen)
        return maxLen

if __name__ == "__main__":
    s = input("Enter the string: ")
    obj = Solution()
    result = obj.maxDepth(s)
    print(result)
