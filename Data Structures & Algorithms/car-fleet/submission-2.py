class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        dic = dict(zip(position, speed))



        des_dic = {k:v for k, v in sorted(dic.items(), key = lambda item: item[0], reverse = True)}

        stac = []

        res = 0

        for des, spe in des_dic.items():
            if len(stac) == 0:
                stac.append((target - des)/spe)
                res += 1

            else:
                current_time = (target - des) / spe

                if current_time <= stac[-1]:
                    continue
                else:
                    stac.append(current_time)
                    res += 1

        return res