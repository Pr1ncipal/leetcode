class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1Tracker = 0
        nums2Tracker = 0
        m = len(nums1)
        n = len(nums2)
        combo = [None] * (n + m)
        p = len(combo)

        for i in range(len(combo)):
            if nums1Tracker == m:  # nums1 is complete
                combo[i] = nums2[nums2Tracker]
                nums2Tracker += 1
            elif nums2Tracker == n:  # nums2 is complete
                combo[i] = nums1[nums1Tracker]
                nums1Tracker += 1
            elif nums1[nums1Tracker] <= nums2[nums2Tracker]:  # nums1 is lower
                combo[i] = nums1[nums1Tracker]
                nums1Tracker += 1
            elif nums2[nums2Tracker] < nums1[nums1Tracker]:  # nums2 is lower
                combo[i] = nums2[nums2Tracker]
                nums2Tracker += 1

        if p % 2 == 0:  # if the array has even length
            return (combo[int((p / 2) - 0.5)] + combo[int((p / 2) + 0.5)]) / 2
        elif p % 2 == 1:  # odd length
            return combo[int(p / 2)]

# First ever leetcode hard completed, learned about the two pointer approach. Honestly, not too bad.
