class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:  
        # def add_word(trie: Mapping, word: str) -> None:
        #     root = trie
        #     for c in word:
        #         if c not in root:
        #             root[c] = {}
        #         root = root[c]
        #     root['#'] = {}

        # def get_words(trie: Mapping, prefix: str) -> List[str]:
        #     if self.k == 0:
        #         return []
        #     res = []
        #     if '#' in trie:
        #         self.k -= 1
        #         res.append(prefix)
        #     for i in range(26):
        #         c = chr(ord('a') + i)
        #         if c in trie:
        #             res += get_words(trie[c], prefix+c)
        #     return res

        # n = len(words)
        # cnt = Counter(words)
        # bucket = [{} for _ in range(n+1)]
        # self.k = k

        # for word, freq in cnt.items():
        #     add_word(bucket[freq], word)

        # res = []
        # for i in range(n, 0, -1):
        #     if self.k == 0:
        #         return res
        #     if bucket[i]:
        #         res += get_words(bucket[i], '')
        # return res

        
        word_count = Counter(words)
        heap = [(-freq, word) for word, freq in word_count.items()]
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result      

        # hm = defaultdict(int)
        # for w in words:
        #     hm[w] += 1

        # min_heap = []
        # for w, count in hm.items():
        #     heapq.heappush(min_heap, (-count, w))

        # result = [heapq.heappop(min_heap)[1] for _ in range(k)]
        # return result

        # hm = defaultdict(int)
        # for w in words:
        #     hm[w] += 1
        # # print(hm)
        # min_heap = []
        # for w, count in hm.items():
        #     if len(min_heap) < k:
        #         heapq.heappush(min_heap, (count, w))               
        #     else:
        #         heapq.heappushpop(min_heap, (count, w))
        # min_heap.sort(key = lambda x: (-x[0], x[1]))
        # return [x[1] for x in min_heap]