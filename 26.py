class Solution:
    def removeDuplicates(nums: list[int]) -> int:
        count = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if i < len_nums -1 and nums[i] == nums[i + 1]:
                continue
            
            nums[count] = nums[i]
            count += 1

        return count




nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])) #5, nums = [0,1,2,3,4,_,_,_,_,_]   

# 0, 0, 1, 1, 2, 2, 3