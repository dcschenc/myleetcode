class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        count_a = count_b = total_ab = 0
        for c in text:
            if c == pattern[1]:
                total_ab += count_a
            if c == pattern[0]:
                count_a += 1

        # Count 'b' after the complete scan for second pattern insertion case
        for c in text:
            if c == pattern[1]:
                count_b += 1

        return max(total_ab + count_b, total_ab + count_a)


        # def get_pattern_num(text):
        #     postsum = [0] * len(text)
        #     cur = 0
        #     for i in range(len(text)-1, -1, -1):
        #         if text[i] == pattern[1]:
        #             cur += 1
        #         postsum[i] = cur
        #     count = 0
        #     for i in range(len(text)-1):
        #         if text[i] == pattern[0]:
        #             count += postsum[i+1]
        #     return count

        # num_a, num_b = 0, 0
        # text_a = pattern[0] + text
        # text_b = text + pattern[1]
        # num_a = get_pattern_num(text_a)
        # num_b = get_pattern_num(text_b)
        # return max(num_a, num_b)