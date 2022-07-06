class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        maxLen = 0

        for num in numSet :
            if num-1 not in numSet:
                curPtr = num + 1
                curLen = 1
                while curPtr in numSet:
                    curLen += 1
                    curPtr += 1
                maxLen = max(maxLen, curLen)

        return maxLen
    