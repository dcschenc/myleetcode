class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = set()
        foods = set()
        mp = Counter()
        for _, table, food in orders:
            tables.add(int(table))
            foods.add(food)
            mp[f'{table}.{food}'] += 1
        foods = sorted(list(foods))
        tables = sorted(list(tables))
        res = [['Table'] + foods]
        for table in tables:
            t = [str(table)]
            for food in foods:
                t.append(str(mp[f'{table}.{food}']))
            res.append(t)
        return res

        hm = defaultdict(lambda:defaultdict(int))
        food = set()
        for c, t, f in orders:
            hm[t][f] += 1
            food.add(f)
        ans = []
        header = ['Table']
        sorted_food = sorted(list(food))
        for f in sorted_food:
            header.append(f)
        ans.append(header)
        for t, foods in sorted(hm.items(), key=lambda x: int(x[0])):
            cur = [t]
            for f in sorted_food:
                cur.append(str(foods[f]))
            ans.append(cur)
        return ans
        