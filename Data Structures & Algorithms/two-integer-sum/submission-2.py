class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for p1 in range(len(nums)):
            complement = target - nums[p1]
            if complement in hash:
                return [hash[complement], p1]
            hash[nums[p1]] = p1
             
        