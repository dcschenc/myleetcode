class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2178.Maximum%20Split%20of%20Positive%20Even%20Integers
        if finalSum % 2:
            return []
        i = 2
        ans = []
        while i <= finalSum:
            ans.append(i)
            finalSum -= i
            i += 2
        ans[-1] += finalSum
        return ans

        def backtrack(cur, path):
            nonlocal ans
            if cur == finalSum:
                if len(path) > len(ans):
                    ans = path
                return True
            # if cur > finalSum: return
            prev = 0
            if len(path) > 0:
                prev = path[-1]
            i = 1
            while cur + prev + 2 * i <= finalSum:
                path.append(prev + 2 * i)
                if backtrack(cur + prev + 2 * i, path):
                    return True
                path.pop()
                i += 1
            return False

        if finalSum % 2 == 1: return []
        ans = []
        backtrack(0, [])
        return ans