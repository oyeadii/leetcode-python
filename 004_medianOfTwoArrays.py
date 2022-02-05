class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        print(nums1)
        if len(nums1)%2==0:
            k= int(len(nums1)/2)
            return (nums1[k]+nums1[k-1])/2
        else:
            return float(nums1[int((len(nums1)-1)/2)])
