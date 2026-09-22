class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = 1
        postfix = 1
        res = [0]*n

        for i in range(n):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        for i in range(n-1, -1, -1):
            res[i]= res[i] * postfix
            postfix = postfix * nums[i]

        return res