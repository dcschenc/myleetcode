class StockPrice:
    # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2034.Stock%20Price%20Fluctuation
    def __init__(self):
        self.prices = defaultdict(int)
        self.max = 0
        self.min = float('inf')
        self.mx_time = 0

    def update(self, timestamp: int, price: int) -> None:
        recal_max, recal_min = False, False
        if timestamp in self.prices:
            if self.max == self.prices[timestamp]:
                recal_max = True
            if self.min == self.prices[timestamp]:
                recal_min = True

        self.prices[timestamp] = price
        if recal_max:
            self.max = max(self.prices.values())
        else:
            self.max = max(self.max, price)
        if recal_min:
            self.min = min(self.prices.values())      
        else:      
            self.min = min(self.min, price)
        self.mx_time = max(self.mx_time, timestamp)        

    def current(self) -> int:
        # t = max(self.prices.keys())
        # return self.prices[t]
        return self.prices[self.mx_time]
        

    def maximum(self) -> int:
        # return max(self.prices.values())
        return self.max

    def minimum(self) -> int:
        # return min(self.prices.values())
        return self.min
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()