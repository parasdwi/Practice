class Solution(object):
    def romanToInt(self, s):
        num=0
        rom={"I": 1,"V": 5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)-1):
            if rom[s[i]]<rom[s[i+1]]:
                num-=rom[s[i]]
            else:
                num+=rom[s[i]]
        return num+rom[s[-1]]
