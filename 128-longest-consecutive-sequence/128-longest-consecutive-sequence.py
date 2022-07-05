class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        ans = 0
        for i in nums :
            if i not in dic :
                left = dic.get(i-1, 0)
                right = dic.get(i+1, 0)
                length = left + right + 1
                ans = max(ans,length)

                dic[i] = length
                dic[i-left] = length
                dic[i+right] = length
        return ans