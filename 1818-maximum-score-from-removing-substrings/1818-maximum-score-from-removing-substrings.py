class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1717.Maximum%20Score%20From%20Removing%20Substrings
        a, b = "a", "b"
        if x < y:
            x, y = y, x
            a, b = b, a
        ans = cnt1 = cnt2 = 0
        for c in s:
            if c == a:
                cnt1 += 1
            elif c == b:
                if cnt1:
                    ans += x
                    cnt1 -= 1
                else:
                    cnt2 += 1
            else:
                ans += min(cnt1, cnt2) * y
                cnt1 = cnt2 = 0
        ans += min(cnt1, cnt2) * y
        return ans    


        # def calculate_score(substring, x, y):
        #     score = 0
        #     stack = []
        #     for char in substring:
        #         if char == 'a' and stack and stack[-1] == 'b':
        #             score += x
        #             stack.pop()
        #         elif char == 'b':
        #             stack.append(char)
        #         else:
        #             stack = []

        #     while stack:
        #         if stack.pop() == 'b':
        #             score += y

        #     return score

        # if x < y:
        #     x, y = y, x
        #     s = s.replace('a', 'c').replace('b', 'a').replace('c', 'b')

        # result = 0

        # ab_score = calculate_score(s, x, y)
        # ba_score = calculate_score(s[::-1], x, y)

        # return max(ab_score, ba_score)


        stack = []        
        i, n = 0, len(s)
        target = 'ab'
        if x < y:
            target = 'ba'
        result = 0
        while i < len(s):
            stack.append(s[i])
            while len(stack) >=2 and ''.join(stack[-2:]) == target:            
                stack.pop()
                stack.pop()
                result += max(x, y)  
            i += 1
        s = ''.join(stack)
        stack = []
        i = 0
        while i < len(s):
            stack.append(s[i])
            while len(stack) >=2 and ''.join(stack[-2:]) == target[::-1]:
                stack.pop()
                stack.pop()
                result += min(x, y)
            i += 1
        return result

        # target = target[::-1]
        # while stack:
        #     if len(stack) >=2 and ''.join(stack[-2:]) == target:
        #         stack.pop()
        #         stack.pop()
        #         result += min(x, y)
        #     else:
        #         stack.pop()
        # return result
            