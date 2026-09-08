class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        emptyMap = {} #Create empty hashmap 

#Target - nums[i] = missingNum
        for i, j in enumerate (nums):
            missingNum = target - nums[i]
            if missingNum in emptyMap:
                return [emptyMap[missingNum],i]
            emptyMap[nums[i]]= i

        return 

            

    