class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Given: string s 
        looking for a substring w/o duplicates --> need somewhere to store as we go!
        Constraints: 0 <= s.length() <= 50,000 --> 10^4< O(n) or O(nlogn) <10^5 

        Longest substring --> two pointers -> Sliding Window

        Similar to Best time to buy stocks with a twist:

        Buy stocks looked in a forward lens such that once you find a new low theres no going back
        [3,4,6,2,8] --> once trade[3,6] prof = 3 -> reach 2 thats your new low

        Can't do that with the substring since you can have test cases where the duplicate 
        doesn't line up with your left pointer
        
        r>F       "pw" was the longest window so far so longestSub = 2
        l
        ["pwwkew"] --> l pointer would have to slide from p to the 2nd w since the dup wasn't p

        so you slide L over by one until you don't have a duplicate in the window
        r>>>F
        l>         "wkei" window = 4 so find max(longestSub, 4) -> 4
        ["wkeiw"]
        
        Coding Up:

        need to store a l, r pointer both starting at 0 
        l: starts the window , r: expands the window
        store current window in set -> You know when theres a dupe
        while s[r] not in set: 
        1.calculate longestSubstring-> max(currMax, (r-l)+1 )
        2.slide r to the right
        
        Else l pointer resets window:
            while len(s) != len(set):
                l +=1 
                

        MVP: Max variable, basic while, l & r 

        ''' 
        l = r = 0

        currWindow = set()
        maxSub = 0 

        if len(s) == 0: return 0
        
        while r< len(s):
            #Slide right if len of window [(r-l)+1] is = len(set())
            #currSub = [(r-l)+1]
            if s[r] in currWindow:
                currWindow.remove(s[l])
                l += 1
            else:
                currWindow.add(s[r])
                maxSub = max(maxSub, (r-l)+1)
                r += 1   
            

        return maxSub

                
















