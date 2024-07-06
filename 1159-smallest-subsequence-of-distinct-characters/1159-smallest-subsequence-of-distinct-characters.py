class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        last_seen = {}
        for i in range(len(s)):
            last_seen[s[i]] = i
        for i in range(len(s)):
            if s[i] in stack:
                continue
            while stack and s[i] < stack[-1] and last_seen[stack[-1]] > i:
                stack.pop()            
            stack.append(s[i])
        return ''.join(stack)
        
        # hm = {}
        # for i in range(len(s)):
        #     if s[i] in hm:
        #         hm[s[i]].append(i)
        #     else:
        #         hm[s[i]] = [i]
        # last_k = ''
        # for k in sorted(hm.keys()):
        #     if last_k == '' or len(hm[k]) == 1:
        #         hm[k] = hm[k][0]
        #     else:
        #         last_idx = hm[last_k]
        #         if hm[k][-1] < last_idx:
        #             hm[k] = hm[k][0]
        #         else:
        #             for cur in hm[k]:
        #                 if cur > last_idx:
        #                     hm[k] = cur
        #                     break
        #     last_k = k
        # result = list(hm.items())
        # result.sort(key = lambda x: x[1])
        # res = ''
        # for k, v in result:
        #     res += k
        # return res
        # stack = []  # Initialize an empty stack to store the subsequence

        # last_occurrence = {char: idx for idx, char in enumerate(s)}

        # for idx, char in enumerate(s):
        #     if char in stack:
        #         continue

        #     while (stack and char < stack[-1] and idx < last_occurrence[stack[-1]]):
        #         stack.pop()

        #     stack.append(char)

        # return ''.join(stack)