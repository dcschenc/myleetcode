class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2655.Find%20Maximal%20Uncovered%20Ranges
        ranges.sort(key=lambda x: x[0])
        prev_end = 0
        ans = []
        for start, end in ranges:
            if start - 1 >= prev_end:
                ans.append([prev_end, start-1])                        
            prev_end = max(prev_end, end + 1)

        if prev_end <= n - 1:
            ans.append([prev_end, n-1])
        return ans
        