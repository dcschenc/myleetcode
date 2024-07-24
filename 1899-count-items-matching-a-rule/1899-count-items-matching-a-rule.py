class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        hm = {'type': 0, 'color': 1, 'name': 2}
        for i in range(len(items)):
            if items[i][hm.get(ruleKey)] == ruleValue:
                cnt += 1
        return cnt
