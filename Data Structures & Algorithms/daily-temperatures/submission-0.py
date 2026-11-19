class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mon_stack = []
        n = len(temperatures)
        res = [0] * n

        for day in range(len(temperatures)):
            
            if len(mon_stack) == 0:
                mon_stack.append(day)
            else:
                while (len(mon_stack) > 0) and (temperatures[mon_stack[-1]] < temperatures[day]) :
                    res[mon_stack[-1]] = day - mon_stack[-1]
                    mon_stack.pop(-1)
                mon_stack.append(day)

        return res