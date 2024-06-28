class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_non_backspace_index(string, start):
            skip_backspaces = 0
            while start >= 0:
                if string[start] == '#':
                    skip_backspaces += 1
                elif skip_backspaces > 0:
                    skip_backspaces -= 1
                else:
                    break
                start -= 1
            return start
        S, T = s, t
        i, j = len(S) - 1, len(T) - 1

        while i >= 0 or j >= 0:
            i = get_next_non_backspace_index(S, i)
            j = get_next_non_backspace_index(T, j)

            if i < 0 and j < 0:
                return True  # Both strings processed and equal

            if (i < 0 and j >= 0) or (i >= 0 and j < 0) or (S[i] != T[j]):
                return False  # One string is longer or characters are not equal

            i -= 1
            j -= 1

        return True

        stack_s, stack_t = [], []
        for c in s:
            if c == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(c)
        for c in t:
            if c == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(c)
        return stack_s == stack_t