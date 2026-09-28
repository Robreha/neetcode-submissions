class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxStreak = 0

        for i in numSet:
            if (i-1) not in numSet:
                currStreak = 1
                while (i+1) in numSet:
                    currStreak +=1
                    i+= 1
                maxStreak = max(currStreak, maxStreak)

        return maxStreak



        

        