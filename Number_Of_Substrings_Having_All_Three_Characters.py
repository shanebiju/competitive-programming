class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r = 0, 0
        length = len(s)
        count = 0
        mydict = {}
        dictlen = 0
        
        while r < length:
            if s[r] not in mydict:
                mydict[s[r]] = 1
                dictlen += 1
            else:
                mydict[s[r]] += 1
                
            while dictlen >= 3:
                mydict[s[l]] -= 1
                if mydict[s[l]] == 0:
                    mydict.pop(s[l])
                    dictlen -= 1
                l += 1
                
            count += (r - l + 1)
            r += 1
            
        return ((length * (length + 1)) // 2) - count

if __name__ == "__main__":
    s = input("Enter the string: ")
    obj = Solution()
    result = obj.numberOfSubstrings(s)
    print("Number of substrings containing all characters:", result)
