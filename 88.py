class Solution:
  def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while j >= 0:
      if i >= 0 and nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        k -= 1
        i -= 1
      else:        
        nums1[k] = nums2[j]
        k -= 1
        j -= 1


Solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)