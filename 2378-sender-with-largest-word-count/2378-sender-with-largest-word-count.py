class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = Counter()
        for user, msg in zip(senders, messages):
            words = msg.split()
            counter[user] += len(words)
        sorted_hm = sorted(counter.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return sorted_hm[0][0]