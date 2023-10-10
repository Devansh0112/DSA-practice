class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        s, e = 0, len(nums)-1
        while s<=e:
            m = (s+e)//2
            min_val = min(min_val, nums[m])

            if nums[m] > nums[e]:
                s = m  + 1
            else:
                e = m - 1

        
        return min_val

        