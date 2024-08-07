class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2561.Rearranging%20Fruits
        cnt = Counter()
        for a, b in zip(basket1, basket2):
            cnt[a] += 1
            cnt[b] -= 1
        mi = min(cnt)
        nums = []
        for x, v in cnt.items():
            if v % 2:
                return -1
            nums.extend([x] * (abs(v) // 2))
        nums.sort()
        m = len(nums) // 2
        return sum(min(x, mi * 2) for x in nums[:m])

        # cnt1, cnt2 = Counter(basket1), Counter(basket2)
        # move1, move2 = Counter(), Counter()

        # for k, v in cnt1.items():
        #     if v > cnt2[k]:
        #         if (v - cnt2[k]) % 2 == 1:
        #             return -1
        #         move1[k] = (v - cnt2[k]) // 2

        # for k, v in cnt2.items():
        #     if v > cnt1[k]:
        #         if (v - cnt1[k]) % 2 == 1:
        #             return - 1
        #         move2[k] = (v - cnt1[k]) // 2

        # if sum(move1.values()) != sum(move2.values()): 
        #     return -1
        # move_total = move1 + move2

        # keys = list(move_total.keys())
        # keys.sort()
        # move = sum(move1.values())
        # i, cost = 0, 0
        # while move > 0:
        #     if move_total[keys[i]] >= move:
        #         cost += keys[i] * move
        #         move = 0
        #     else:
        #         cost += keys[i] * move_total[keys[i]]
        #         move -= move_total[keys[i]]
        # return cost        