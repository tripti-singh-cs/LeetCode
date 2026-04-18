class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            ch = chr((columnNumber % 26) + 65)
            ans = ch + ans
            columnNumber //= 26
        
        return ans