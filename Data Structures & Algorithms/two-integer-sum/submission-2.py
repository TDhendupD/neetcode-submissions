class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in map:
                return [map.get(val), i]
            map[num] = i
