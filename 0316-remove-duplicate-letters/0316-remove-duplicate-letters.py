class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        last_index = {}

        for i in range(len(s)):
            last_index[s[i]] = i

        stack = []

        visited = set()

        for i in range(len(s)):

            current_char = s[i]

            if current_char in visited:
                continue

            while stack and current_char < stack[-1] and i < last_index[stack[-1]]:

                removed_char = stack.pop()

                visited.remove(removed_char)

            stack.append(current_char)

            visited.add(current_char)

        return ''.join(stack)