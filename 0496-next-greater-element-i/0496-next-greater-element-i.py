class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for x in nums1:

            index = nums2.index(x)

            found = -1

            for i in range(index + 1, len(nums2)):

                if nums2[i] > x:
                    found = nums2[i]
                    break

            ans.append(found)

        return ans
        