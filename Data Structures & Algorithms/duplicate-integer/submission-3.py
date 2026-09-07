class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Hash Sets
        empty= set()

        for i in nums:
            if i in empty:
                return True
            else: empty.add(i)
        return False





        
