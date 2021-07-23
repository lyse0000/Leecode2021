class Solution:
    def intToRoman(self, num: int) -> str:
        chart = [[1000,'M'],
                 [900,'CM'],
                 [500,'D'],
                 [400,'CD'],
                 [100,'C'],
                 [90,'XC'],
                 [50,'L'],
                 [40,'XL'],
                 [10,'X'],
                 [9,'IX'],
                 [5,'V'],
                 [4,'IV'],
                 [1,'I']]
        
        ret = ""
        for i in range(len(chart)):
            ret += ((num//chart[i][0])*chart[i][1])
            num = num%chart[i][0]
        return ret
            
            
