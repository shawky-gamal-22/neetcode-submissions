class TimeMap:

    def __init__(self):
        
        self.dic = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        current_status = self.dic.get(key, [])

        if len(current_status) == 0:
            current_status = [None] * (10**7 + 1)
        
        current_status[timestamp] = value

        self.dic[key] = current_status
        return None

    def get(self, key: str, timestamp: int) -> str:
        
        current_status = self.dic.get(key, [])
        if len(current_status) == 0:
            return ""

        flag = True 
        i = timestamp
        while flag:

            if current_status[i] is None:
                i = i - 1
            else:
                return current_status[i]
            
            if i == -1 :
                break
        return ""

