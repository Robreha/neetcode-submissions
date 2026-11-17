class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        rob1 = i-2
        rob2 = i-1
        maxRob = (rob1 + nums, rob2)

        You swap between rob1 & rob2, using 
    
        '''
        if len(nums) == 1: return nums[0] #Only 1 element --> [2] -> 2

        return max(self.gotRobbed(nums[:-1]), self.gotRobbed(nums[1:])) 
        #Everything except last vs Everything except the first

    
    def gotRobbed(self, houses):
        rob1 = rob2 = 0

        for num in houses:
            maxRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = maxRob
        
        return rob2