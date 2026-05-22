class Solution:
    def longestPalindrome(self, s: str) -> int:

        frequency = {}

        for ch in s:

            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

        palindrome_length = 0

        odd_character_found = False

        for count in frequency.values():

            if count % 2 == 0:

                palindrome_length += count

            else:
 
                palindrome_length += count - 1

                odd_character_found = True

        if odd_character_found:

            palindrome_length += 1

        return palindrome_length