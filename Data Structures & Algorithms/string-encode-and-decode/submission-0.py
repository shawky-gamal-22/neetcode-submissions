class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")

        return "".join(res)
    def decode(self, s: str) -> List[str]:
        
        res = []

        n = len(s)
        i = 0

        while i < n :
            dell = s.find("#", i)
            length = int(s[i:dell])

            start = dell + 1 
            end = start + length

            res.append(s[start: end])
            i =end

            

        return res