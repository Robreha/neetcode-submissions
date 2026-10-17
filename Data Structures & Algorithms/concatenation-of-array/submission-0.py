class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums * 2)

        for i in range(len(nums)):
            ans[i] = nums[i]
            for j in range(len(ans)):
                ans[i + len(nums)] = nums[i]

        return ans