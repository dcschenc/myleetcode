class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2201.Count%20Artifacts%20That%20Can%20Be%20Extracted
        def find(r1, c1, r2, c2):
            for i in range(r1, r2+1):                
                for j in range(c1, c2+1):
                    if (i, j) not in dig_set:
                        return False
            return True

        dig_set = set()
        for i, j in dig:
            dig_set.add((i, j))
        ans = 0
        for r1, c1, r2, c2 in artifacts:
            if find(r1, c1, r2, c2):
                ans += 1
        return ans
