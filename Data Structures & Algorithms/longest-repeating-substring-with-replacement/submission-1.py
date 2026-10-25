class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        charSet = set(s)

        for c in charSet:
            count = l = 0

            for r in range(len(s)): #Right pointer 
                if s[r] == c: #Right index contiues the streak ex: [a,a, s[r]] -> [a, a, a]
                    count +=1 #Streak counter
                
                #window = (r - l) + 1
                while (r - l) + 1 - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                res = max(res, (r - l) + 1)
        return res