import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        banned_words = set(banned)
        word_count = Counter()
        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        most_common = word_count.most_common(1)
        return most_common[0][0] if most_common else ""
