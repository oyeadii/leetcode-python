class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0 and len(nums1)!=0:
            for i in range(len(nums1)):
                nums1.remove(0)
        for i in range(len(nums1)-m):
            nums1.remove(0)
        for i in range(n):
            nums1.append(nums2[i])
 
        nums1.sort()
