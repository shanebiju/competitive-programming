class Solution:
    def substrCount(self, s, k):
        # your code here
        def LTE(s, target):
            if target == -1 or target == 0:
                return 0
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
                while dictlen > target:
                    mydict[s[l]] -= 1
                    if mydict[s[l]] == 0:
                        mydict.pop(s[l])
                        dictlen -= 1
                    l += 1
                count += (r - l + 1)
                r += 1
            return count
        
        return LTE(s, k) - LTE(s, k - 1)

if __name__ == "__main__":
    # Input from the user
    s = input("Enter the string: ")
    k = int(input("Enter the value of k: "))
    
    # Creating an instance of the Solution class
    obj = Solution()
    
    # Calling the substrCount method and printing the result
    result = obj.substrCount(s, k)
    print("The count of substrings:", result)
