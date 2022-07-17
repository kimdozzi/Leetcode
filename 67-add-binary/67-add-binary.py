class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = str(int(a) + int(b))
        s = ''
        h = 0
        for i in res[::-1] :
            if h :
                i = str(int(i) + 1)
                h -= 1
                
            if i == '0' :
                s = '0' + s
            elif i == '1' :
                s = '1' + s
            elif i == '2' :
                h += 1
                s = '0' + s
            elif i == '3':
                h += 1
                s = '1' + s
                
        if h :
            s = '1' + s
        return s