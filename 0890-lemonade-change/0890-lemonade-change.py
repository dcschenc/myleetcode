class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for v in bills:
            if v == 5:
                five += 1
            elif v == 10:
                ten += 1
                five -= 1
            else:
                if ten:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0:
                return False
        return True
        
        hm = {}
        for i in range(len(bills)):
            if bills[i] == 5:
                hm['5'] = 1 + hm.get('5',0)
            elif bills[i] == 10:
                if hm.get('5', 0) < 1:
                    return False
                hm['5'] = hm['5'] - 1
                hm['10'] = 1 + hm.get('10', 0)
            else:
                if hm.get('10', 0) < 1:
                    if hm.get('5', 0) < 3:
                        return False
                    hm['5'] = hm['5'] - 3                
                else:
                    if hm.get('5', 0) < 1:
                        return False
                    hm['10'] = hm['10'] - 1
                    hm['5'] = hm['5'] - 1
                # hm['20'] = 1 + hm.get('20', 0)
        return True