class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[0] * i for i in range(1,numRows+1)]
        
        for i in range(numRows):
            lst[i][0], lst[i][-1] = 1, 1
            
            for j in range(1,i):                
                lst[i][j] = lst[i-1][j] + lst[i-1][j-1]
        
        return lst
                
            