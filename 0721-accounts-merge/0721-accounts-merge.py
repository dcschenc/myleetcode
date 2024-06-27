from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(email, component):
            if email not in visited:
                visited.add(email)
                component.append(email)
                for neighbor in graph[email]:
                    dfs(neighbor, component)

        email_to_name = {}
        graph = defaultdict(set)
        # Build the graph
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email_to_name[account[i]] = name
                graph[account[i]].update(account[1:i])
                graph[account[i]].update(account[i+1:])

        result = []
        visited = set()

        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                result.append([email_to_name[email]] + sorted(component))
        return result

        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                elif rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                else:
                    rank[rootX] += 1
                    root[rootY] = rootX
            
        adj = defaultdict(list)
        hm = {}
        for acc in accounts:
            for i in range(1, len(acc)):
                for j in range(i+1, len(acc)):
                    adj[acc[i]].append(acc[j])
                    adj[acc[j]].append(acc[i])
                hm[acc[i]] = acc[0]

        root = {}
        rank = defaultdict(int)
        for email in hm.keys():
            root[email] = email
        
        emails = list(hm.keys())
        for i in range(len(emails)):
            for j in range(i+1, len(emails)):
                if emails[j] in adj[emails[i]] or emails[i] in adj[emails[j]]:
                    union(emails[i], emails[j])
        res = defaultdict(list)
        for email in hm.keys():
            root_email = find(email)
            res[root_email].append(email)
        ans = []
        for email in res.keys():
            tmp = []
            tmp.append(hm.get(email))
            tmp.extend(sorted(res[email]))
            ans.append(tmp)
        return ans
