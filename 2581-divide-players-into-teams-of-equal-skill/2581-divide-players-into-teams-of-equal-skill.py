class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2491.Divide%20Players%20Into%20Teams%20of%20Equal%20Skill
        skill.sort()
        ans = 0
        i, j = 0, len(skill) - 1
        total = skill[i] + skill[j]
        while i < j:
            if skill[i] + skill[j] != total:
                return -1
            ans += skill[i] * skill[j]
            i += 1
            j -= 1
        return ans
