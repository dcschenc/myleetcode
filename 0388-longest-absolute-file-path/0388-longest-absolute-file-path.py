class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        max_len = 0
        for s in input.split('\n'):
            depth = s.count('\t')
            name = s.replace('\t', '') 
            while depth < len(stack):
                stack.pop()
            if '.' in name:
                # It's a file
                max_len = max(max_len, len('/'.join(stack + [name])))
            else:
                # It's a directory
                stack.append(name)
        return max_len


        # cur = ''
        # ans = 0
        # arr = input.split("\n")
        # if len(arr) == 0:
        #     return 0
        # if len(arr) == 1:
        #     if '.' in arr[0]:
        #         return len(arr[0])
        #     else:
        #         return 0

        # print(arr)
       
        # for i in range(len(arr)):
        #     cnt = arr[i].count('\t')         
        #     if cnt == 0:
        #         stack = []
        #         root = arr[i]
        #         if '.' in arr[i]:
        #             ans = max(ans, len(arr[i]))
        #     elif cnt == 1:
        #         stack = [(root, 0), (arr[i], 1)]
        #         if '.' in arr[i]:                    
        #             ans = max(ans, len(root) + len(arr[i]))                    
        #     else:
        #         if '.' in arr[i]:
        #             cur = 0
        #             for name, c in stack:
        #                 # print(name, c)
        #                 cur += len(name) - c + 1
        #             # print(arr[i], len(arr[i]))
        #             cur += len(arr[i]) - cnt
        #             ans = max(ans, cur)
        #         else:
        #             while stack and cnt <= stack[-1][1]:
        #                 stack.pop()
        #             stack.append((arr[i], cnt))
        #     print(cnt, stack)

        # return ans                
                

        # for i in range(1, len(arr)):
        #     if arr[i][0] != '\':
        #         cur = root + arr[0]
        #     else:
        #         arr[i-1].count('\t')
        #         cur = cur + arr[i][2:]
        #         if 