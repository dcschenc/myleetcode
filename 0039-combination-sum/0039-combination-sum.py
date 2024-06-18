class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, cur, path):
            if cur == target:
                result.append(path[:])
                return 

            for i in range(start, n):
                if cur + candidates[i] > target: break          
                backtrack(i, cur + candidates[i], path + [candidates[i]])

        n, result = len(candidates), []
        candidates.sort()
        backtrack(0, 0, [])
        return result

        ####### O(N^target) ########
        # def backtrack(candidates, curr):
        #     if len(curr) > 0:
        #         if sum(curr) == target:
        #             res.append(curr)
        #             return True
        #         if sum(curr) > target:
        #             return False
        #     for i, val in enumerate(candidates):
        #         # curr.append(val)
        #         prune = backtrack(candidates[i:],curr + [val])
        #         # curr.pop()
        #         if prune == False:
        #             break
        
        # def backtrack(start, target, current_combination):
        #     if target == 0:
        #         result.append(current_combination[:])
        #         return
        #     if target < 0:
        #         return

        #     for i in range(start, len(candidates)):
        #         if candidates[i] > target:
        #             break  # Prune the branch if the current candidate is too large
        #         current_combination.append(candidates[i])
        #         backtrack(i, target - candidates[i], current_combination)
        #         current_combination.pop()

        # result = []
        # candidates.sort()
        # backtrack(0, target, [])
        # return result