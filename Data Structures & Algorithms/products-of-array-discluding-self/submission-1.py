class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_inds = []
        for i in range(len(nums)):
            if nums[i] != 0:
                product*=nums[i]
            else:
                zero_inds.append(i)
        if len(zero_inds) >= 2:
            return [0] * len(nums)
        if len(zero_inds) == 1:
            result = [0] * len(nums)
            result[zero_inds[0]] = product
            return result
        return [product // num for num in nums]
            
            
