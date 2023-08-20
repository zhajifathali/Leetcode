class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} # create dict
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i