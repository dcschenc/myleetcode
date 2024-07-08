class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr12 = []
        arr = []
        arr1 = Counter(arr1)
        for i in arr2:
            arr12 += [i] * arr1[i]
            
        for i in arr1:
            if i not in arr2:
                arr += [i] * arr1[i]
        return arr12 + sorted(arr)
       
        # # arr2 = set(arr2)
        # hm = defaultdict(int)
        # not_in_arr2 = []
        # arr2set = set(arr2)
        # for num in arr1:
        #     if num in arr2set:                
        #         hm[num] += 1
        #     else:
        #         not_in_arr2.append(num)
        # res = []
        # for num in arr2:
        #     for i in range(hm[num]):
        #         res.append(num)
        # not_in_arr2.sort()
        # res.extend(not_in_arr2)
        # return res
        