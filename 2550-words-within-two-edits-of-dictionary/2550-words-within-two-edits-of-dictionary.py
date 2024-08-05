class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2452.Words%20Within%20Two%20Edits%20of%20Dictionary
        ans = []
        for q in queries:
            for w in dictionary:
                if sum([a != b for a, b in zip(q, w)]) <= 2:
                    ans.append(q)
                    break
        return ans