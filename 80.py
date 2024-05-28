class Solution:
    def removeDuplicates(nums: list[int]) -> int:
        slow, fast = 0, 2
        while fast in range(len(nums)):
            if nums[slow] != nums[fast]:    
                nums[slow+2] = nums[fast]
                slow += 1
            fast += 1

        print(nums)
        return slow + 2

print(Solution.removeDuplicates(nums = [1,1,2,2,2,3]))