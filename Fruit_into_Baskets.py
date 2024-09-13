class Solution:
    def totalFruits(self, arr):
        # Your logic here
        dictlen = 0
        mydict = {}
        l, r = 0, 0
        maxLength = 0
        length = len(arr)
        
        while r < length:
            if arr[r] not in mydict:
                mydict[arr[r]] = 1
                dictlen += 1
            else:
                mydict[arr[r]] += 1
            
            if dictlen > 2:
                mydict[arr[l]] -= 1
                if mydict[arr[l]] == 0:
                    mydict.pop(arr[l])
                    dictlen -= 1
                l += 1
            
            if dictlen <= 2:
                maxLength = max(maxLength, r - l + 1)
            r += 1
        
        return maxLength

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    
    obj = Solution()
    result = obj.totalFruits(arr)
    
    print("The maximum number of fruits that can be collected is:", result)
