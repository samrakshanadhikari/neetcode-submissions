class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #so first make a dictionary and sort all items and [put] a main key the sorted one and value as a list and at last return all dicitonary values
        groups={}
        for word in strs:

            key=" ".join(sorted(word))
            if key not in groups:
                groups[key]=[] #start an empty list
            
            groups[key].append(word) #append the word act in the list
        
        return list(groups.values())

        

        


        

        