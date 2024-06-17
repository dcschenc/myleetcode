class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # nums.sort()
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:  # reduce duplicate
        #         continue
        #     target = 0 - nums[i]
        #     hashtable = {}
        #     for j in range(i+1, len(nums)):
        #         d = target - nums[j]
        #         if d in hashtable:
        #             if hashtable[d] > 1:  # reduce duplicate
        #                 continue
        #             hashtable[d] += 1
        #             res.append([nums[i], d, nums[j]])
        #         else:
        #             hashtable[nums[j]] = 1
        # return res

        nums.sort()       
        n = len(nums)
        res = []
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ == 0:
                    res.append([nums[i], nums[j], nums[k]])                    
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif sum_ < 0:
                    j += 1
                else:
                    k -= 1
        return res
    
#         hm = {}
#         # res = []
#         for i in range(n):
#             for j in range(i+1,n):               
#                 k = nums[i] + nums[j]
#                 if k in hm:
#                     hm[k].append((i,j))
#                 else:
#                     hm[k] = [(i,j)]
#         res = []
#         # print(hm)
#         for k in hm.keys():
#             values = hm[k]
#             for v in values:
#                 i, j = v[0], v[1]
#                 m = j+1
#                 while m < n:
#                     if nums[m] == -k:
#                         if [nums[i], nums[j], nums[m]] not in res:
#                             res.append([nums[i],nums[j],nums[m]])
                        
#                         break
#                     m+=1
#                 # for m in range(j+1, n):
#                 #     if nums[m] > -k:
#                 #         break
#                 #     elif nums[m] == k:
#                 #         
#                                 #             res.append([nums[i],nums[j],nums[m]])
#                 #         break
#         return res