import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Convert paragraph to lowercase and split it into words.
        words = re.findall(r'\w+', paragraph.lower())

        # Create a set of banned words for efficient lookup.
        banned_words = set(banned)

        # Create a Counter to count word occurrences.
        word_count = Counter()

        # Count the occurrences of each word, excluding banned words.
        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        # Find the most common word using the Counter.
        most_common = word_count.most_common(1)

        return most_common[0][0] if most_common else ""

        # cur = ''
        # words = []
        # hm = {}
        # n = len(paragraph)
        # for i, c in enumerate(paragraph):
        #     if c.isalpha():
        #         cur = cur + c.lower()
        #     if (c in "!?',;. " or i == n - 1) and cur != '':
        #         hm[cur] = 1 + hm.get(cur, 0)
        #         cur = ''           
        # max_l = 0
        # ans = ''
        # for k, v in hm.items():
        #     if k not in banned and v > max_l:
        #         max_l = v
        #         ans = k
        # return ans
