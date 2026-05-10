from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        last_index = {}

        for i in range(len(nums)):

            current_num = nums[i]

            # check if number already seen
            if current_num in last_index:

                # check distance between indices
                if i - last_index[current_num] <= k:
                    return True

            # store/update latest index
            last_index[current_num] = i

        return False