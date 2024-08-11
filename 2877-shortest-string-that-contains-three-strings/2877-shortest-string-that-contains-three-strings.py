class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2800.Shortest%20String%20That%20Contains%20Three%20Strings
        def merge(s1: str, s2: str) -> str:
            # Check if one string is a subsequence of the other and return the longer one.
            if s1 in s2:  return s2
            if s2 in s1:  return s1
          
            # Identify the longest common suffix of s1 and prefix of s2
            # Then merge s1 and s2 by overlapping this common part
            len_s1, len_s2 = len(s1), len(s2)
            for overlap_length in range(min(len_s1, len_s2), 0, -1):
                if s1[-overlap_length:] == s2[:overlap_length]:
                    return s1 + s2[overlap_length:]
          
            # If there is no overlap, concatenate the strings
            return s1 + s2

        # Initialize the answer with an empty string.
        ans = ""
      
        # Check all permutations of the input strings to find the shortest merged string
        for x, y, z in permutations((a, b, c)):
            merged_string = merge(merge(x, y), z)
            if not ans or len(merged_string) < len(ans) or (len(merged_string) == len(ans) and merged_string < ans):
                ans = merged_string

        # Return the shortest string found
        return ans


        # def check(x, y):
        #     if y in x:
        #         return len(y) + 1
        #     idx = 0
        #     for i in range(1, len(y)):                
        #         if y[:i] == x[-i:]:
        #             idx = i
        #     return idx

        # idx_ab = check(a, b)
        # idx_ac = check(a, c)
        # idx_ba = check(b, a)
        # idx_bc = check(b, c)
        # idx_ca = check(c, a)
        # idx_cb = check(c, b)        

        # candidate = [a, b, c]
        # abc = a
        # if b not in abc:
        #     abc += b[idx_ab:]  
        # if c not in abc:     
        #     abc += c[idx_bc:]

        # acb = a
        # if c not in acb:
        #     acb += c[idx_ac:]
        # if b not in acb:
        #     acb += b[idx_cb:]

        # bac  = b
        # if a not in bac:
        #     bac += a[idx_ba:]
        # if c not in bac:
        #     bac += c[idx_ac:]

        # bca = b
        # if c not in bca:
        #     bca += c[idx_bc:]
        # if a not in bca:
        #     bca += a[idx_ca:]

        # cab = c
        # if a not in cab:
        #     cab += a[idx_ca:]
        # if b not in cab:
        #     cab += b[idx_ab:]

        # cba = c
        # if b not in cba:
        #     cba += b[idx_cb:]
        # if a not in cba:
        #     cba += a[idx_ba:]

        # ans, length = '', float('inf')
        # print([abc, acb, bac, bca, cab, cba])
        # for cur in [abc, acb, bac, bca, cab, cba]:
        #     if len(cur) < length:
        #         ans = cur
        #         length = len(cur)
        #     elif len(cur) == length:
        #         if ans > cur:
        #             ans = cur
        # return ans

