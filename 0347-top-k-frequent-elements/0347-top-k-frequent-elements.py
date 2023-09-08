class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] += 1
        
        sort_values = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        
        print('hasmap : {0} and sorted : {1}'.format(hash_map, sort_values))
        
        res = [i[0] for i in sort_values]
        
        return res[:k]
        
        