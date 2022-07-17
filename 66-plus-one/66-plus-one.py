class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''
        for i in digits :
            res += str(i)
        res = int(res) + 1
        lst = list(map(int,str(res)))
        return lst