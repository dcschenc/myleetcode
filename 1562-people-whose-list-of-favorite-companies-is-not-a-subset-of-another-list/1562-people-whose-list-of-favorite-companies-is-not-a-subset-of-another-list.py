class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:        
        # O(n^2 * k)
        favorites = [set(x) for x in favoriteCompanies]
        ans = []
        for i in range(len(favorites)):
            found = False
            for j in range(len(favorites)):
                if i == j or len(favorites[i]) > len(favorites[j]):
                    continue
                if favorites[i].issubset(favorites[j]):
                    found = True
                    break
            if found is False:
                ans.append(i)
        return ans
