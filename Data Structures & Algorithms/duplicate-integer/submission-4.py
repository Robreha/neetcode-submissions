class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Hash Sets
        if len(set(nums)) < len(nums):
            return True 
        return False




'''
 #Brute force method —> Too slow 
        n= len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False 
  
  #Sort method
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums [i+1]:
                return True
        return False


#Hash Sets
        empty= set()

        for i in nums:
            if i in empty:
                return True
            else: empty.add(i)
        return False
'''


        
