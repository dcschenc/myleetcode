class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:       
        if len(nums) <= 1:
            return nums
        pivot = len(nums)//2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        if i < len(left):
            res.extend(left[i:])
        if j < len(right):
            res.extend(right[j:])
        return res

        # ######## quick sort #######
        # if len(nums) <= 1:
        #     return nums
    
        # pivot = nums[len(nums) // 2]
        # left = [x for x in nums if x < pivot]
        # middle = [x for x in nums if x == pivot]
        # right = [x for x in nums if x > pivot]
        
        # return sortArray(left) + middle + sortArray(right)

        # def partition(low, high):
        #     pivot = nums[high]
        #     i = low - 1

        #     for j in range(low, high):
        #         if nums[j] <= pivot:
        #             i += 1
        #             nums[i], nums[j] = nums[j], nums[i]

        #     nums[i + 1], nums[high] = nums[high], nums[i + 1]
        #     return i + 1

        # def quickSort(low, high):
        #     if low < high:
        #         pivot_index = partition(low, high)
        #         quickSort(low, pivot_index - 1)
        #         quickSort(pivot_index + 1, high)

        # quickSort(0, len(nums) - 1)
        # return nums

        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        if len(nums) <= 1:
            return nums

        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]

        left = self.sortArray(left)
        right = self.sortArray(right)

        return merge(left, right)