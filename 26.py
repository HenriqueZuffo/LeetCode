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
        
        # Second approach to resolve 
        # slow, fast = 0, 1
        # while fast in range(len(nums)):
        #     if nums[slow] == nums[fast]:
        #         fast += 1
        #     else:
        #         nums[slow+1] = nums[fast]
        #         fast += 1
        #         slow += 1

        # print(nums)
        # return slow + 1        

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])) #5, nums = [0,1,2,3,4,_,_,_,_,_]   

# 0, 0, 1, 1, 2, 2, 3