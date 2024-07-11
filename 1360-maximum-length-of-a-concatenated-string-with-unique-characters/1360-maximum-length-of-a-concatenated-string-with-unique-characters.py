class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1239.Maximum%20Length%20of%20a%20Concatenated%20String%20with%20Unique%20Characters
        def backtrack(idx, cur):            
            ans[0] = max(ans[0], len(cur))
            if idx == n:  return
            for i in range(idx, n):
                if all(c not in cur for c in arr[i]) and len(arr[i]) == len(set(arr[i])):
                    backtrack(i + 1, cur + arr[i])
        ans = [0]
        n = len(arr)
        backtrack(0, '') 
        return ans[0]