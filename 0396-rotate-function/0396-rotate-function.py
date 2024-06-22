class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        n = len(nums)
    
        # Calculate the initial value of F(0)
        f0 = sum(i * nums[i] for i in range(n))
        
        # Calculate the sum of all elements in the input array A
        array_sum = sum(nums)
        
        max_rotation = f0  # Initialize the maximum rotation value with F(0)
        current_rotation = f0  # Initialize the current rotation value
        
        for k in range(1, n):
            # Use the formula to calculate F(k) based on F(k-1)
            current_rotation = current_rotation + array_sum - n * nums[n - k]            
            # Update the maximum rotation value if the current rotation is larger
            max_rotation = max(max_rotation, current_rotation)
        
        return max_rotation

        # ans=0
        # s=sum(nums)
        # xsum=0
        # ret=0
        # for i in range(len(nums)):
        #     xsum=xsum+i*nums[i]
        # ret=xsum
        # ans=xsum
        # for i in range(len(nums)-1,-1,-1):
        #     ans=(ans+s-len(nums)*nums[i])
        #     if ans>ret:
        #         ret=ans
       
        # return ret
            