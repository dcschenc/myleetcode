class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2591.Distribute%20Money%20to%20Maximum%20Children
        if money < children:
            return -1
        if money > 8 * children:
            return children - 1
        if money == 8 * children - 4:
            return children - 2
        # money-8x >= children-x, x <= (money-children)/7
        return (money - children) // 7