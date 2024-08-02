class ATM:
    def __init__(self):
        self.cnt = [0] * 5
        self.d = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, v in enumerate(banknotesCount):
            self.cnt[i] += v

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        for i in range(4, -1, -1):
            ans[i] = min(amount // self.d[i], self.cnt[i])
            amount -= ans[i] * self.d[i]
        if amount > 0:
            return [-1]
        for i, v in enumerate(ans):
            self.cnt[i] -= v
        return ans


# class ATM:

#     def __init__(self):
#         self.hm = defaultdict(int)        
#         self.notes = [20, 50, 100, 200, 500]

#     def deposit(self, banknotesCount: List[int]) -> None:
#         for note, num in zip(self.notes, banknotesCount):
#             self.hm[note] += num      

#     def withdraw(self, amount: int) -> List[int]:
#         ans = []
#         # original = amount
#         for note, num in sorted(self.hm.items(), reverse=True):
#             if amount == 0:
#                 ans.append(0)
#                 continue
#             n = amount // note
#             n = min(num, n)
#             ans.append(n)
#             amount -= n * note

#         ans.reverse()        
#         # if sum([note * num for note, num in zip(self.notes, ans)]) != original:           
#         if amount != 0:
#             return [-1]
#         for note, num in zip(self.notes, ans):
#             self.hm[note] -= num
        
#         return ans


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)