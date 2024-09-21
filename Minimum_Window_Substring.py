class Solution:
    def minWindow(self, str1: str, str2: str) -> str:
        def freqCheck(dict2, dict1):
            for x in dict2:
                if dict2[x] > dict1.get(x, 0):
                    return False
            return True
        
        dict2 = {}
        for x in str2:
            dict2[x] = dict2.get(x, 0) + 1
        
        dict1 = {}
        length = len(str1)
        l, r = 0, 0
        ansLen = float('inf')
        ans = (0, 0)
        
        while r < length:
            dict1[str1[r]] = dict1.get(str1[r], 0) + 1
            
            while set(dict2.keys()).issubset(dict1.keys()) and freqCheck(dict2, dict1):
                if ansLen > r - l + 1:
                    ansLen = r - l + 1
                    ans = (l, r)
                
                dict1[str1[l]] -= 1
                if dict1[str1[l]] == 0:
                    dict1.pop(str1[l])
                l += 1
            
            r += 1
        
        return str1[ans[0]:ans[1]+1] if ansLen != float('inf') else ""

if __name__ == "__main__":
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    solution = Solution()
    result = solution.minWindow(str1, str2)
    print("Minimum window substring:", result)
