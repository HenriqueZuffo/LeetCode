class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        i = 0

        for num in nums:
            if num != val:
                nums[i] = num
                i += 1

        print(i)
        return i
