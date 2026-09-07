class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #one shot
        return sorted(s) == sorted (t)

        '''
        if len(s)!= len(t): #Length of strings have to be equal to be anagram
            return False
        
        countS, countT= {}, {} #Create hashmaps to store strings

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countS[t[i]] = 1 + countS.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True
        '''
        
