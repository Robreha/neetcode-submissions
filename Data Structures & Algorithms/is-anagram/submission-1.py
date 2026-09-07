class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


    '''
        string1= set(s)
        string2= set(t)

        if string1 == string2:
            return True
        return False
    '''