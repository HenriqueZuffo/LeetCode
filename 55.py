class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        goal = n -1

        for i in range(n-1, -1, -1):
            jump = nums[i]                               
            if i + jump >= goal:
                goal = i
        
        return goal == 0




s = Solution()
print(s.canJump(nums = [2,3,1,1,4]))          