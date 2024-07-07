class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
            n = len(books)
            dp = [float('inf')] * (n + 1)
            dp[0] = 0
            for i in range(1, n + 1):
                width = 0
                max_height = 0
                j = i
                # for each previou `book[j]`, verify if it can be placed in the same row as `book[i]`
                while j > 0:   
                    width += books[j - 1][0]  # Width of the current book
                    if width > shelfWidth:
                        break
                    max_height = max(max_height, books[j - 1][1])  # Height of the current book
                    dp[i] = min(dp[i], dp[j - 1] + max_height)
                    j -= 1

            return dp[n]