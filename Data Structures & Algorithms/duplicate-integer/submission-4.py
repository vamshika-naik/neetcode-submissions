class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = defaultdict(list)
        for i in nums:
            if i in res:
                return True
            res[i].append(i)
        return False