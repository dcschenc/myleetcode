class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        prev_b = 0
        for b, p in brackets:
            if b < income:
                tax += (b - prev_b) * p
            else:
                tax += (income - prev_b) * p
                break
            prev_b = b
        return tax / 100