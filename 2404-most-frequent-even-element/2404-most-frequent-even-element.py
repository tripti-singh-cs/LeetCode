class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        
        # count frequency of even numbers
        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0) + 1
        
        if not freq:
            return -1
        
        max_freq = 0
        result = float('inf')
        
        for num, count in freq.items():
            if count > max_freq or (count == max_freq and num < result):
                max_freq = count
                result = num
        
        return result