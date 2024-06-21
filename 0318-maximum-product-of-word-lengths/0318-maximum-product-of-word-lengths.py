class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_length = [len(word) for word in words]
        words_set = [set(word) for word in words]
        max_len = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not words_set[i] & words_set[j]:
                    max_len = max(max_len, words_length[i]*words_length[j])
        return max_len