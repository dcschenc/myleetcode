class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(s[-4:-2]) > 60 for s in details)
