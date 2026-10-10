class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        
        profit = 0
        buy = prices[r] #current low

        while r< len(prices):
            if prices[r] < buy: #If new low
                buy= prices[r]
                l= r
            #sell = max(sell, prices[r])
            profit = max(profit, prices[r] - buy)
            r +=1

        if profit <0:
            return 0

        return profit


        '''
        *Can only look forward so prices[r] has to be > current min
        1.Find the low within the window
            [low, r]
        2. Iterate with r pointer 
            a)If new r is smaller then reset your pointers there
            b)Calcualate max prof at each index
        '''
        
