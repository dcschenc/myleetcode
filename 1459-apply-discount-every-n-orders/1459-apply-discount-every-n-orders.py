class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        # self.products = products
        # self.prices = prices
        self.product_price = {}
        for product, price in zip(products, prices):
            self.product_price[product] = price
        self.cur = 1
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        for p, amount in zip(product, amount):
            bill += self.product_price[p] * amount
        if self.cur % self.n == 0:
            bill = bill * (100 - self.discount) / 100
        self.cur += 1
        return bill

        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)