class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1

        magical_string = [1, 2, 2]
        i = 2  # Index to generate the next characters
        while len(magical_string) < n:
            magical_string.extend([3 - magical_string[-1]] * magical_string[i])
            i += 1

        return magical_string[:n].count(1)        