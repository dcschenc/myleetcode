class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        d = defaultdict(list)
        idx = set()
        for i, x in enumerate(transactions):
            name, time, amount, city = x.split(",")
            time, amount = int(time), int(amount)
            d[name].append((time, city, i))
            if amount > 1000:
                idx.add(i)
            for t, c, j in d[name]:
                if c != city and abs(time - t) <= 60:
                    idx.add(i)
                    idx.add(j)
        return [transactions[i] for i in idx]
        
        # trans = []
        # result = []
        # idx = set()        
        # for i, t in enumerate(transactions):
        #     (name, time, amount, city) = t.split(',')
        #     trans.append({ 'name': name, 'time': int(time), 'amount': int(amount), 'city': city, 'index':i})

        # trans.sort(key=lambda x: (x['name'], x['time']))
        # for i, t in enumerate(trans):
        #     if t['amount'] >= 1000:                
        #         idx.add(t['index'])            
        #     for j in range(i+1, len(trans)):
        #         if t['name'] != trans[j]['name']:
        #             break
        #         if abs(t['time'] - trans[j]['time']) > 60:
        #             break
        #         if t['city'] != trans[j]['city']:
        #             idx.add(t['index'])
        #             idx.add(trans[j]['index'])
        # for i in idx:
        #     result.append(transactions[i])
        # return result


        