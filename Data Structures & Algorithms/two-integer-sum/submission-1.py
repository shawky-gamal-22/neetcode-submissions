class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq= {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1 

        for i in range(len(nums)):
            res = target - nums[i]

            if freq.get(res, 0) == 0:
                continue
            
            for z in range(i + 1 , len(nums)):
                if nums[z] == res :
                    return [i, z]

