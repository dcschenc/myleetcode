class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        mod = purchaseAmount % 10
        div = purchaseAmount // 10
        if mod >= 5:
            div += 1
        return 100 - div * 10