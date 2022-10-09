# faster then 98.56% online submissions

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        i,sum=len(columnTitle)-1,0
        j=0
        while(0<=i<len(columnTitle)):
            sum+=(26**(i))*(ord(columnTitle[j])-64)
            j+=1
            i-=1
        return sum
