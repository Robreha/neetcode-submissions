class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Sort method: Sort strings then check if they're equal to each other 
        O(m * nlogn) --> Slow
        '''
        
        '''
        HashMap: O(m * n * 26)->O(m*n)
        1.Create array count to store number occurences for each letter
        2.Create hashMap with [key, value]->[count, strs[i]]
        '''
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ...z

            for c in s:
                count[ord(c)- ord('a')] += 1

            res[tuple(count)].append(s)
        
        return list(res.values())

            
