from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []

        def is_palindrome(word):

            return word == word[::-1]

        def backtrack(start, path):

            if start == len(s):

                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):

                current = s[start:end]

                if is_palindrome(current):

                    path.append(current)

                    backtrack(end, path)

                    path.pop()

        backtrack(0, [])

        return result