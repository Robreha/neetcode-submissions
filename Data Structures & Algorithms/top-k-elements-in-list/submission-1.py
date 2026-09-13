class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        nums.sort() #Sorts list nums

        num_Occurences = {} # Empty dict

        for i in nums: #Adds [key,value]->[number, frequency] to a hashmap
            num_Occurences[i] = num_Occurences.get(i, 0) + 1 

        sorted_Occurences = list(num_Occurences.items()) #Initliaze tuple = dict so you can sort

        sorted_Occurences = sorted(num_Occurences.items(), key=lambda x: x[1], reverse=True)

        top_k = sorted_Occurences[:k]

        return [pair[0] for pair in top_k]

        
