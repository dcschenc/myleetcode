class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2559.Count%20Vowel%20Strings%20in%20Ranges
        vowels = set("aeiou")
        nums = [i for i, w in enumerate(words) if w[0] in vowels and w[-1] in vowels]
        return [bisect_right(nums, r) - bisect_left(nums, l) for l, r in queries]

        n = len(words)
        pre = [0] * (n + 1)
        for i, w in enumerate(words):
            pre[i + 1] = pre[i]
            if w[0] in 'aeiou' and w[-1] in 'aeiou':
                pre[i + 1] = pre[i] + 1                
        ans = []
        for l, r in queries:
            ans.append(pre[r + 1] - pre[l])
        return ans
        