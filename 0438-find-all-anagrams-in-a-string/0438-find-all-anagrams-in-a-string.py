from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0438.Find%20All%20Anagrams%20in%20a%20String
        n, m = len(s), len(p)
        if n < m: return []
        count_s = Counter(s[:m-1])
        count_p = Counter(p)
        left = 0
        ans = []
        for right in range(m-1, n):
            count_s[s[right]] += 1
            if count_s == count_p:
                ans.append(left)
            count_s[s[left]] -= 1            
            left += 1
        return ans

        # res = []
        # length = len(p)
        # hm_p = defaultdict(int)
        # hm_s = defaultdict(int)
        # if len(p) > len(s):
        #     return []
        # for c in p:
        #     hm_p[c]+=1
        # for i in range(len(p)):
        #     hm_s[s[i]]+=1
        # if hm_p == hm_s:
        #     res.append(0)
        # for i in range(len(p),len(s)):
        #     k = s[i-length]
        #     if hm_s[k] == 1:
        #         del hm_s[k]
        #     else:
        #         hm_s[k]-=1           
        #     hm_s[s[i]] += 1
        #     # print(i, hm_s)
        #     if hm_p == hm_s:
        #         res.append(i-length+1)
        # return res
        # res = []
        # length = len(p)
        # p_counter = Counter(p)
        # for i in range(len(s)):
        #     if Counter(s[i:i+length]) == p_counter:
        #         res.append(i)
        # return res