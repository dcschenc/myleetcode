class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1733.Minimum%20Number%20of%20People%20to%20Teach
        # Convert the 1-based index to 0-based index for easier manipulation
        languages = [set(lang) for lang in languages]
        
        # Identify all the communication gaps
        need_teaching = set()
        for u, v in friendships:
            u, v = u - 1, v - 1  # convert to 0-based index
            if not languages[u] & languages[v]:  # if no common language
                need_teaching.add(u)
                need_teaching.add(v)
        
        if not need_teaching:
            return 0  # no need to teach anyone
        
        # Calculate the minimum number of people to teach for each language
        min_teach = float('inf')
        for lang in range(1, n + 1):
            teach_count = 0
            for person in need_teaching:
                if lang not in languages[person]:
                    teach_count += 1
            min_teach = min(min_teach, teach_count)
        
        return min_teach

        languages = {u + 1: set(l) for u, l in enumerate(languages)}
        s = set()
        for u, v in friendships:
            if not languages[u] & languages[v]:
                s.add(u)
                s.add(v)
        cnt = Counter()
        for u in s:
            for l in languages[u]:
                cnt[l] += 1
        return len(s) - max(cnt.values(), default=0)

