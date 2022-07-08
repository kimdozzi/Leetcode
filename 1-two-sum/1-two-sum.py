class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i in range(len(nums)) :
            for j in range(i,len(nums)) :
                if i == j :
                    continue
                if nums[i] + nums[j] == target :
                    lst.append(i)
                    lst.append(j)
        
        lst.sort()
        return lst
    