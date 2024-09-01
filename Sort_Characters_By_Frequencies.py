class Solution:
    def frequencySort(self, s: str) -> str:
        mydict = {}
        ans = ""
        for x in s:
            if x not in mydict:
                mydict[x] = 1
            else:
                mydict[x] += 1
        mydict = dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
        for key in mydict:
            ans += key * mydict[key]
        return ans

if __name__ == "__main__":
    s = input()
    sol = Solution()
    result = sol.frequencySort(s)
    print(result)
