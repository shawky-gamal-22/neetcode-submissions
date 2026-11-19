class Solution:

    def encode(self, strs: List[str]) -> str:
        
        s = ""
        for i in strs:
            s+=f"{i}|-|"
        return s
    def decode(self, s: str) -> List[str]:
        
        l=[]
        st=""
        return s.split("|-|")[:-1]