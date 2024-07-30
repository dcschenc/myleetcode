from collections import deque, defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:        
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2115.Find%20All%20Possible%20Recipes%20from%20Given%20Supplies
        g = defaultdict(list)
        indeg = defaultdict(int)
        for a, b in zip(recipes, ingredients):
            for v in b:
                g[v].append(a)
            indeg[a] += len(b)
        q = deque(supplies)
        ans = []
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                for j in g[i]:
                    indeg[j] -= 1
                    if indeg[j] == 0:
                        ans.append(j)
                        q.append(j)
        return ans
        
        # adj = defaultdict(list)
        # hm = {}
        # degree = {re: 0 for re in recipes}
        # for i in range(len(recipes)):
        #     hm[recipes[i]] = set(ingredients[i])
        #     for j in range(len(ingredients[i])):
        #         if ingredients[i][j] in recipes:
        #             adj[ingredients[i][j]].append(recipes[i])
        #             degree[recipes[i]] += 1
        
        # result = set()
        # queue = deque()
        # supplies = set(supplies)
        # candidates = set()
        # # candidates = set(adj.keys())
        # # print(adj.keys(), candidates)
        # for re in recipes:
        #     if degree[re] == 0:
        #         candidates.add(re)
        # for re in candidates:
        #     if hm[re].issubset(supplies):
        #         queue.append(re)
        # # print(queue)
        # while queue:
        #     for i in range(len(queue)):
        #         re = queue.popleft()
        #         if re in result:
        #             continue
        #         supplies.add(re)
        #         result.add(re)
        #         for nb in adj[re]:
        #             degree[nb] -= 1
        #             # hm[nb].remove(re)
        #             if degree[nb] == 0 and hm[nb].issubset(supplies) :
        #                 queue.append(nb)
        # return result


               
        