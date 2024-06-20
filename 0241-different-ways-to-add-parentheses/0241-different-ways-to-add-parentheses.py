class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []
        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])                
                for l in left:
                    for r in right:
                        if expression[i] == "+":
                            results.append(l + r)
                        elif expression[i] == "-":
                            results.append(l - r)
                        elif expression[i] == "*":
                            results.append(l * r)

        # If there are no operators in the expression, add the integer itself to the result
        if not results:
            results.append(int(expression))

        return results