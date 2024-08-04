class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2383.Minimum%20Hours%20of%20Training%20to%20Win%20a%20Competition
        cur_energy, cur_exp = initialEnergy, initialExperience
        ans = 0
        for en, ex in zip(energy, experience):
            if cur_exp <= ex:
                ans += (ex - cur_exp + 1)
                cur_exp = ex + 1
            if cur_energy <= en:
                ans += (en - cur_energy + 1)
                cur_energy = 1                
            else:
                cur_energy -= en
            cur_exp += ex
        return ans
            

