class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2766.Relocate%20Marbles
        seen = set(nums)
        for f, t in zip(moveFrom, moveTo):
            if f!= t and f in seen:
                seen.remove(f)
                seen.add(t)
        return sorted(list(seen))

        # counter = Counter(nums)
        # for f, t in zip(moveFrom, moveTo):
        #     if f!= t and f in counter:
        #         counter[t] += counter[f]
        #         del counter[f]
        # return sorted(counter.keys())
            