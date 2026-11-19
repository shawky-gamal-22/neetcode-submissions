class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 


        se = set(nums)
        
        max_len = 0
        for s in se:
            if freq.get(s - 1, 0) > 0:
                continue
            
            else:
                flag = True
                lenn = 1
                i = 1
                while flag:
                    if freq.get(s + i, 0) > 0:
                        lenn += 1
                        i +=1
                    else:
                        flag= False
                if lenn > max_len :
                    max_len = lenn
        return max_len
