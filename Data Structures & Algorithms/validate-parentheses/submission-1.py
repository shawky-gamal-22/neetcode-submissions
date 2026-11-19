class Solution:
    def isValid(self, s: str) -> bool:
        
        lis = []

        for c in s:

            if c in ["(", "{", "["]:
                lis.append(c)
            elif len(lis) == 0 :
                lis.append(c)
            elif c == ")":
                if lis[-1] == "(":
                    lis.pop(-1)
                else:
                    lis.append(c)
            elif c == "}":
                if lis[-1] == "{":
                    lis.pop(-1)
                else:
                    lis.append(c)
            elif c == "]":
                if lis[-1] == "[":
                    lis.pop(-1)
                else:
                    lis.append(c)

        if len(lis) > 0:
            return False
        return True
        