class Solution:
    def countSegments(self, s: str) -> int:
        
        # split string into words
        words = s.split()

        # return total number of words
        return len(words)