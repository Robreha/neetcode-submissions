class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Find target in Rotated Array-> So trick is finding which half is still sorted

        Simpler: Binary search on sorted array find target, if target not found return -1
        '''
        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r - l) // 2 

            if nums[m] == target:
                return m

            #Left Sorted portion
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            #Right Sorted portion
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else: 
                    r = m - 1
                
        return -1

    





