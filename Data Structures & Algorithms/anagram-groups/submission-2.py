class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dc = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in dc:
                dc[key] = []
            dc[key].append(s)
        
        return list(dc.values())