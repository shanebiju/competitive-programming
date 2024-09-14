class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mydict = {}
        length = len(s)
        l, r = 0, 0
        maxLength = 0
        while r < length:
            if s[r] not in mydict:
                mydict[s[r]] = 1
            else:
                mydict[s[r]] += 1
            while (r - l + 1) - max(mydict.values()) > k:
                mydict[s[l]] -= 1
                if mydict[s[l]] == 0:
                    mydict.pop(s[l])
                l += 1
            maxLength = max(maxLength, r - l + 1)
            r += 1
        return maxLength


if __name__ == "__main__":
    s = input()
    k = int(input())
    obj = Solution()
    result = obj.characterReplacement(s, k)
    print(result)
