class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        res = [0]*(len(nums))

        for i in range (len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        for i in range (len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            

        return res



    """
    - They want O(n) space and time so I can make a new array for results
    -Want to calculate prefix and postfix at each index --> prefix * postfix = res[i]
    -Brute force would be double for loop checking every combo

    1.prefix iterates forward until i, postifx goes backwards from len(nums)-1 until i
    2. when you reach i set res[i]= postfix * prefix
    """