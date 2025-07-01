class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}  # Dictionary to store previous values and their indices

        for i, num in enumerate(nums):
            difference = target - num
            
            if difference in prev_map:
                return [prev_map[difference], i]
            
            prev_map[num] = i
        
        raise ValueError("No match found!")