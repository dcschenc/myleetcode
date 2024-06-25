class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0498.Diagonal%20Traverse
        m, n = len(mat), len(mat[0])
        ans = []
        for k in range(m + n - 1):
            t = []
            i = 0 if k < n else k - n + 1
            j = k if k < n else n - 1
            while i < m and j >= 0:
                t.append(mat[i][j])
                i += 1
                j -= 1
            if k % 2 == 0:
                t = t[::-1]
            ans.extend(t)
        return ans

        d={}
		#loop through matrix
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                #if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                #If you've already passed over this diagonal, keep adding elements to it!
                    d[i+j].append(mat[i][j])
        # we're done with the pass, let's build our answer array
        ans= []
        #look at the diagonal and each diagonal's elements
        for k, v in d.items():
            if k%2 == 0:
                ans.extend(v[::-1])
            else:
                ans.extend(v)
        # for entry in d.items():
        #     if entry[0] % 2 == 0:
        #         [ans.append(x) for x in entry[1][::-1]]
        #     else:
        #         [ans.append(x) for x in entry[1]]
        return ans


        # m, n = len(mat), len(mat[0])
        # res = []
        # reverse = False       

        # for i in range(m):
        #     level_res = []
        #     tmp_i = i
        #     j = 0
        #     while tmp_i >=0 and j < n:
        #         level_res.append(mat[tmp_i][j])
        #         tmp_i -= 1
        #         j += 1

        #     if reverse is True:
        #         level_res = level_res[::-1]
        #         reverse = False
        #     else:
        #         reverse = True
        #     res.extend(level_res)

        # for j in range(1, n):
        #     i = m-1
        #     level_res = []
        #     tmp_j = j
        #     while i >= 0 and tmp_j < n:
        #         level_res.append(mat[i][tmp_j])
        #         i -= 1
        #         tmp_j += 1
            
        #     if reverse is True:
        #         level_res = level_res[::-1]
        #         reverse = False
        #     else:
        #         reverse = True
        #     res.extend(level_res)
        # return res
