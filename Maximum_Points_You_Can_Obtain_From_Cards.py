class Solution:
    def maxScore(self, cardPoints, k):
        # code here.
        left = 0
        length = len(cardPoints)
        right = k
        windowSum = sum(cardPoints[length-right:length])
        maxSum = windowSum
        right = k - 1
        
        while right != -1:
            left = k - right
            windowSum = windowSum - cardPoints[length-right-1] + cardPoints[left-1]
            maxSum = max(maxSum, windowSum)
            right = right - 1
            
        return maxSum

if __name__ == "__main__":
    k = int(input("Enter the value of k: "))
    cardPoints = list(map(int, input("Enter the card points separated by space: ").split()))
    obj = Solution()
    result = obj.maxScore(cardPoints, k)
    print("Maximum score:", result)
