class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newarray = nums1 + nums2

        result = sorted(newarray)

        length = len(result)

        if length % 2 == 1:
            return float(result[length // 2])

        else:
            mid1 = result[(length // 2) - 1]
            mid2 = result[length // 2]
            return (mid1 + mid2) / 2.0

       