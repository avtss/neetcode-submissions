class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el_count = {}
        for el in nums:
            if el not in el_count.keys():
                el_count[el] = 1
            else:
                el_count[el] += 1
        count = len(nums) // 2
        res = 0
        for k, v in el_count.items():
            if v > count:
                return k