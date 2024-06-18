class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        left = 0
        right = n - 1
        left_max = right_max = 0
        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -= 1

        return trapped_water

        # left = [0]*len(height)
        # max_left = 0
        # for i, h in enumerate(height):
        #     if i == 0:
        #         left[0] = max_left
        #     else:
        #         left[i] = max_left
        #     if h > max_left:
        #         max_left = h

        # # right = []
        # max_right = 0
        # res = 0
        # # height.reverse()
        # i = len(height)-1
        # while i >0:
        #     h = height[i]
        #     if left[i] > max_right:
        #         res += max(max_right - h, 0)
        #     else:
        #         res += max(left[i] - h, 0)
        #     if h > max_right:
        #         max_right = h
        #     i-=1
        # return res