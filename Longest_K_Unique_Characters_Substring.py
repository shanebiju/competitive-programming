class Solution:
    def longestKSubstr(self, s, k):
        # Code here
        dictlen = 0
        mydict = {}
        maxLength = -1
        l, r = 0, 0
        length = len(s)

        while r < length:
            if s[r] not in mydict:
                mydict[s[r]] = 1
                dictlen += 1
            else:
                mydict[s[r]] += 1

            if dictlen > k:
                mydict[s[l]] -= 1
                if mydict[s[l]] == 0:
                    mydict.pop(s[l])
                    dictlen -= 1
                l += 1

            if dictlen == k:
                maxLength = max(maxLength, r - l + 1)

            r += 1

        return maxLength


if __name__ == "__main__":
    s = input("Enter the string: ")
    k = int(input("Enter the value of k: "))
    obj = Solution()
    result = obj.longestKSubstr(s, k)
    print("The length of the longest substring with exactly", k, "distinct characters is:", result)
