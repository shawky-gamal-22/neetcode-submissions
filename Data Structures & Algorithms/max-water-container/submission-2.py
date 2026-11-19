class Solution:
    def maxArea(self, heights: List[int]) -> int:
        st = 0
        ed = len(heights) - 1
        max_area = 0

        while st < ed:
            current_len = min(heights[st], heights[ed])
            current_wid = ed - st 
            max_area = max(max_area, current_len * current_wid)

            if (heights[st] > heights[ed]) :
                ed = ed - 1
            elif (heights[st] <= heights[ed]):
                st = st + 1
            
        return max_area
 