class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        p1 = 0
        while p1 < len(nums):
            if nums[p1] not in unique:
                unique.add(nums[p1])
                p1 += 1
            else:
                return True
        return False
        