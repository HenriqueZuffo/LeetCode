class Solution:
    def jump(self, nums: list[int]) -> int:
        steps = 0
        ans = 0
        end = 0

        for i in range(len(nums) - 1):

            steps = max(steps, i + nums[i])
            
            if steps >= len(nums) - 1:
                ans += 1
                break


            if i == end:      
                ans += 1 
                end = steps

        return ans





s = Solution()
print(s.jump(nums = [2,3,1,1,4]))          