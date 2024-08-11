# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2782.Number%20of%20Unique%20Categories
        cats = set()
        cats.add(0)
        for i in range(1, n):            
            if any(categoryHandler.haveSameCategory(i, j) for j in cats):
                continue
            cats.add(i)
        return len(cats)

