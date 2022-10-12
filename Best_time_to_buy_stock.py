class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i,j,pro=0,1,0
        while(j<len(prices)):
            if prices[i]<prices[j]:
                pro=max(pro,prices[j]-prices[i])
            else:
                i=j
            j+=1
        return pro
