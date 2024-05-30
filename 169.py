class Solution:
    def majorityElement(nums: list[int]) -> int:
        m = None
        count = 0

        for num in nums:
            if count == 0:
                m = num
            
            if num == m:
                count += 1
            else:
                count -= 1

        return m
        


print(Solution.majorityElement(nums = [2,2,1,1,1,2,2]))