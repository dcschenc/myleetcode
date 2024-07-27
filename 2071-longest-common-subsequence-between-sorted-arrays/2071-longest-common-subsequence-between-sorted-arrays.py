class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)
        counter = defaultdict(int)
        for array in arrays:
            for e in array:
                counter[e] += 1
        return [e for e, count in counter.items() if count == n]

        
        m = len(arrays)             
        cols = [0] * m
        length = [len(arrays[i]) for i in range(m)]
        ans = []    
        while all (cols[i] < length[i] for i in range(m)):           
            cur = []
            for i in range(m):                
                cur.append(arrays[i][cols[i]])
           
            if len(set(cur)) == 1:
                ans.append(cur[0])
                for i in range(m):
                    cols[i] += 1
            else:
                min_v = min(cur)                
                for i in range(m):
                    if cur[i] == min_v:
                        cols[i] += 1
        return ans