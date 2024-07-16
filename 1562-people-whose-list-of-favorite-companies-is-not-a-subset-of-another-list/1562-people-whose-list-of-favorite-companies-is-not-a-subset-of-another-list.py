class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # def isSubset(l1, l2):
        #     for w in l1:
        #         if w not in l2:
        #             return False
        #     return True
        
        # O(n^2 * k)
        favorites = [set(x) for x in favoriteCompanies]
        ans = []
        for i in range(len(favorites)):
            found = False
            for j in range(len(favorites)):
                if i == j or len(favorites[i]) > len(favorites[j]):
                    continue
                # if isSubset(favorites[i], favorites[j]):
                if favorites[i].issubset(favorites[j]):
                    found = True
                    break
            if found is False:
                ans.append(i)
        return ans

        # d = {}
        # idx = 0
        # t = []
        # for v in favoriteCompanies:
        #     for c in v:
        #         if c not in d:
        #             d[c] = idx
        #             idx += 1
        #     t.append({d[c] for c in v})
        # ans = []
        # for i, nums1 in enumerate(t):
        #     ok = True
        #     for j, nums2 in enumerate(t):
        #         if i == j:
        #             continue
        #         if not (nums1 - nums2):
        #             ok = False
        #             break
        #     if ok:
        #         ans.append(i)
        # return ans        d = {}
        # idx = 0
        # t = []
        # for v in favoriteCompanies:
        #     for c in v:
        #         if c not in d:
        #             d[c] = idx
        #             idx += 1
        #     t.append({d[c] for c in v})
        # ans = []
        # for i, nums1 in enumerate(t):
        #     ok = True
        #     for j, nums2 in enumerate(t):
        #         if i == j:
        #             continue
        #         if not (nums1 - nums2):
        #             ok = False
        #             break
        #     if ok:
        #         ans.append(i)
        # return ans