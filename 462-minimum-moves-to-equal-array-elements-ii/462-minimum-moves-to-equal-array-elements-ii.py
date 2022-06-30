class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        count=0
        nums.sort() 
        l = len(nums) // 2
        mid = nums[l]
        for num in nums:
            count += abs(mid-num)
        return count
    
        
        
        
        
                
        
                
        