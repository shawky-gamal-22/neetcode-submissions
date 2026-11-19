class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lis = []

        for token in tokens:
            
            if token == "+":
                num2 = lis[-1]
                lis.pop(-1)
                num1 = lis[-1]
                lis.pop(-1)

                lis.append(num1 + num2)
            elif token == "-":
                num2 = lis[-1]
                lis.pop(-1)
                num1 = lis[-1]
                lis.pop(-1)

                lis.append(num1 - num2)
            elif token == "*":
                num2 = lis[-1]
                lis.pop(-1)
                num1 = lis[-1]
                lis.pop(-1)

                lis.append(num1 * num2)
            elif token == "/":
                num2 = lis[-1]
                lis.pop(-1)
                num1 = lis[-1]
                lis.pop(-1)

                lis.append(int(num1 / num2))

            else:
                lis.append(int(token))

        return lis[-1]