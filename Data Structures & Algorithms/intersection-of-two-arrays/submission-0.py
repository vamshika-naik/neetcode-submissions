class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []
        for i in nums1:
            for j in nums2:
                if i == j and i not in inter:
                    inter.append(i)
        return inter