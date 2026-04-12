from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0

        while l < r:
            width = r - l

            if height[l] < height[r]:
                area = height[l] * width
                l += 1
            else:
                area = height[r] * width
                r -= 1

            if area > ans:
                ans = area

        return ans  