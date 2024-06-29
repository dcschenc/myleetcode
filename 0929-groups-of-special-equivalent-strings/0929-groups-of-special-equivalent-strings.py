class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        counter = Counter()
        for w in words:
            odd, even = '', ''
            for i, c in enumerate(w):
                if i % 2 == 0:
                    even += c
                else:
                    odd += c
            key = ''.join(sorted(odd)) + ''.join(sorted(even))
            counter[key] += 1
        return len(counter.keys())

        