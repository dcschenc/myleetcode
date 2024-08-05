class Solution:
    def robotWithString(self, s: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2434.Using%20a%20Robot%20to%20Print%20the%20Lexicographically%20Smallest%20String
        cnt, stack, ans = Counter(s), [], []
        for c in s:
            stack.append(c)
            cnt[c] -= 1
            if cnt[c] == 0:
                del cnt[c]
            while cnt and stack and min(cnt) >= stack[-1]:
                ans += stack.pop()
            
        ans += stack[::-1]
        return ''.join(ans)

        cnt = Counter(s)
        ans = []
        stk = []
        mi = 'a'
        for c in s:
            cnt[c] -= 1
            while mi < 'z' and cnt[mi] == 0:
                mi = chr(ord(mi) + 1)
            stk.append(c)
            while stk and stk[-1] <= mi:
                ans.append(stk.pop())
        return ''.join(ans)
        
        dic, t, ans = Counter(s), [], []
        for char in s:
            t.append(char)
            if dic[char] == 1:
                del dic[char]
            else:
                dic[char] -= 1
            while dic and t and min(dic) >= t[-1]:
                ans += t.pop()
        ans += t[::-1]
        return ''.join(ans)