class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1540.Can%20Convert%20String%20in%20K%20Moves
        if len(s) != len(t):
            return False
        
        # Frequency array to count the required shifts
        shift_count = [0] * 26

        # Calculate the necessary shifts
        for i in range(len(s)):
            if s[i] != t[i]:
                shift = (ord(t[i]) - ord(s[i])) % 26
                shift_count[shift] += 1

        # Check if we can make the shifts within k moves
        for shift in range(1, 26):
            if shift_count[shift] > 0:
                max_moves_needed = shift + (shift_count[shift] - 1) * 26
                if max_moves_needed > k:
                    return False

        return True
        
        if len(s) != len(t): return False
        n, hm = len(s), defaultdict(int)
        for a, b in zip(s, t):
            if a == b: continue
            diff = (ord(b) - ord(a)) % 26
            # if diff < 0:
                # diff = diff + 26
            hm[diff] += 1

        for d, cnt in hm.items():
            for i in range(cnt):
                if d + 26 * i > k:
                    return False
        return True


            