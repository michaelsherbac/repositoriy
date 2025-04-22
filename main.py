class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        i = 0
        while i < len(nums):
            for j in range(len(nums) - 1, -1, -1):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
            i += 1