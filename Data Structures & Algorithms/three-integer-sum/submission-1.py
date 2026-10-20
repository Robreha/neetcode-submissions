class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        i + j + k = 0 so -> j+k = -i
        Approaches: Def want set for O(1) lookups
        for every i check if 2 numbers exist that sum to -i

        Wants O(n^2) and O(1) space --> So no set just maybe 2 pointers and nest for loop

        for i in nums: -> find elements such that i = -(j + k) return nums[i],[j],[k]
        -append the working combos to an empty list
        -

        '''

        
        nums.sort()

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: #Duplicate cases [-1, -1 , 2] -> Skips second -1
                continue 
            l , r = i+1 , len(nums)-1
            while l < r:
                current = nums[l] + nums[r]
                target = -nums[i]
                if target > current: #under estimate
                    l += 1
                elif target < current: #over estimate
                    r -= 1
                else:
                    res.append([nums[i], nums[l],nums[r]]) #Valid guess
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        return res



