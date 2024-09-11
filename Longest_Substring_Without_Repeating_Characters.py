class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength=0
        length=len(s)
        l,r=0,0
        mydict={}
        while r<length:
            if s[r] not in mydict or mydict[s[r]]<l:
                mydict[s[r]]=r
            else:
                l=mydict[s[r]]+1
                mydict[s[r]]=r
            maxLength=max(maxLength,r-l+1)
            r+=1
        return maxLength

if __name__ == "__main__":
    # Input from the user
    s = input("Enter a string: ")
    
    # Creating an instance of the Solution class
    obj = Solution()
    
    # Calling the lengthOfLongestSubstring method and printing the result
    result = obj.lengthOfLongestSubstring(s)
    print("Length of the longest substring without repeating characters:", result)