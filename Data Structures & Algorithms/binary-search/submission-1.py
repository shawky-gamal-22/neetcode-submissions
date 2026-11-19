class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        ed = len(nums) - 1
        mid = (ed + st) // 2

        

        while st <= ed:

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                ed = mid - 1
            
            else:
                st = mid + 1 

            mid = (ed + st) // 2

        return -1