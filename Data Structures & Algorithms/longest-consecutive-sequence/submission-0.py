class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if (num-1) in numset:
                continue
            else:
                cur = num
                curlen = 1
                while cur+1 in numset:
                    cur+=1
                    curlen+=1
            longest = max(longest, curlen)
        return longest
            
            
                    
        