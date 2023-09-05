class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(len(nums)):
            number2 = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == number2:
                    return [i,j]
