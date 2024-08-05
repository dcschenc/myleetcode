class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2456.Most%20Popular%20Video%20Creator
        cnt = defaultdict(int)
        d = defaultdict(int)
        for k, (c, i, v) in enumerate(zip(creators, ids, views)):
            cnt[c] += v
            if c not in d or views[d[c]] < v or (views[d[c]] == v and ids[d[c]] > i):
                d[c] = k
        mx = max(cnt.values())
        return [[c, ids[d[c]]] for c, x in cnt.items() if x == mx]

        
        # hm = {}
        # for i, creator in enumerate(creators):
        #     if creator not in hm:
        #         hm[creator] = {'total': views[i], 'most_id': ids[i], 'most_view': views[i]}
        #     else:
        #         hm[creator]['total'] += views[i]
        #         if views[i] > hm[creator]['most_view'] or views[i] == hm[creator]['most_view'] and ids[i] < hm[creator]['most_id']:
        #             hm[creator]['most_id'] = ids[i]
        #             hm[creator]['most_view'] = views[i]

        # sorted_items = sorted(hm.items(), key=lambda x: x[1]['total'], reverse=True)
        # most_popular = sorted_items[0][1]['total']
        # result = []
        # for k, v in sorted_items:
        #     if v['total'] == most_popular:
        #         result.append([k, v['most_id']])
        # return result
