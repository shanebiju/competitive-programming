class Solution:
    def romanToInt(self, s: str) -> int:
        mydict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        length=len(s)
        ans=0
        i=0
        if len(s)==1:
            return mydict[s[0]]
        while i<length-1:
            if mydict[s[i]]>=mydict[s[i+1]]:
                ans+=mydict[s[i]]
                i=i+1
            else:
                ans+=(mydict[s[i+1]]-mydict[s[i]])
                i+=2
        if mydict[s[-2]]>=mydict[s[-1]]:
            ans+=mydict[s[-1]]
        return ans

if __name__ == "__main__":
    s = input("Enter a Roman numeral string: ")
    solution = Solution()
    result = solution.romanToInt(s)
    print("Integer value:", result)
