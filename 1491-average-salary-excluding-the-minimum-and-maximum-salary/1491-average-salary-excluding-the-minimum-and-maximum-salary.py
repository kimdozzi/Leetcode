class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop()
        res = 0
        cnt = 0
        for i in salary :
            res += i
            cnt += 1
        return (res / cnt)