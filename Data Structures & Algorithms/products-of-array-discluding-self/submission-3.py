class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Store prefix, postfix, product= post * pre, append to res[]
        n = len(nums)
        pre= 1
        post=1
        product= 1  #pre * post
        res = [0]*n

        for i in range (n):
           res[i] = pre
           pre = pre * nums[i]

        for i in range (n-1, -1, -1):
            res[i] *= post   
            post = post * nums[i]
        
        return res