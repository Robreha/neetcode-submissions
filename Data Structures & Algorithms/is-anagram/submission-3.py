class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Sort method --> one shot
        #return sorted(s) == sorted (t)

        
        if len(s)!= len(t): #Length of strings have to be equal to be anagram
            return False
        
        countS, countT= {}, {} #Create hashmaps to store # of strings

        for i in range(len(s)): #Both strings have the same length
            countS[s[i]] = 1 + countS.get(s[i], 0) #Count of each letter
            countT[t[i]] = 1 + countT.get(t[i], 0) 

        #Now have 2 hash maps with the number of occurences of each letter
        return countS == countT #Check if they're equal
        
        
