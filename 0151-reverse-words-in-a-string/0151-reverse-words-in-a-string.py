class Solution:
    def reverseWords(self, s: str) -> str:
        #split words (removes extra spaces)
        words = s.split()
        
        #reverse words
        words = words[::-1]
        
        #join with single space
        return " ".join(words)