class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0842.Split%20Array%20into%20Fibonacci%20Sequence
        def dfs(i):
            if i == n: return len(ans) > 2
            x = 0
            for j in range(i, n):
                if j > i and num[i] == '0':
                    break
                x = x * 10 + int(num[j])
                if x > 2**31 - 1 or (len(ans) > 2 and x > ans[-2] + ans[-1]):
                    break
                if len(ans) < 2 or ans[-2] + ans[-1] == x:
                    ans.append(x)
                    if dfs(j + 1):
                        return True
                    ans.pop()
            return False

        n = len(num)
        ans = []
        dfs(0)
        return ans

        # def backtrack(idx):
        #     if idx == n: return len(path) >= 3              
        #     elif len(path) >= 2:
        #         target = str(path[-1] + path[-2])
        #         if path[-1] + path[-2] <= 2 ** 31 - 1:                    
        #             if idx + len(target) <= n and target == num[idx:idx + len(target)]:
        #                 path.append(int(target))
        #                 if backtrack(idx + len(target)):
        #                     return True
        #                 path.pop()
        #     else:
        #         if num[idx] == '0':
        #             path.append(0)
        #             if backtrack(idx + 1):
        #                 return True
        #             path.pop()
        #         else:
        #             for i in range(idx + 1, n+1):   
        #                 if int(num[idx:i]) > 2**31 -1:
        #                     break      
        #                 path.append(int(num[idx:i]))               
        #                 if backtrack(i):
        #                     return True
        #                 path.pop()
        #     return False
        # n = len(num)
        # path = []
        # if backtrack(0):
        #     return path
        # return []
        
        # def backtrack(idx, path):
        #     # print(idx, path)
        #     if idx == n:
        #         if len(path) >= 3:
        #             return path[:]
        #         else:
        #             return []

        #     if len(path) >= 2:
        #         target = str(path[-1] + path[-2])
        #         if path[-1] + path[-2] > 2 ** 31 - 1:
        #             return []
        #         if idx + len(target) <= n and target == num[idx:idx + len(target)]:
        #             res = backtrack(idx + len(target), path + [int(target)])
        #             if res != []:
        #                 return res
        #     else:
        #         if num[idx] == '0':
        #             res = backtrack(idx + 1, path + [0])
        #             if res != []:
        #                 return res
        #         else:
        #             for i in range(idx + 1, n+1):   
        #                 if int(num[idx:i]) > 2**31 -1:
        #                     break                     
        #                 res = backtrack(i, path + [int(num[idx:i])])
        #                 if res != []:
        #                     return res
        #     return []
        # n = len(num)
        # path = backtrack(0, [])
        # return path