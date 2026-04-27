class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in seen and seen[rem] != i:
                return sorted([i, seen[rem]])
            seen[nums[i]] = i