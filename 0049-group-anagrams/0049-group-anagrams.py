from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))   # sort characters
            ans[sorted_word].append(word)         # store original word

        return list(ans.values())