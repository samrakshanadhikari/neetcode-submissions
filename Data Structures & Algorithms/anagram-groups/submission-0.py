class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #so we can do something like first sort all the strings in the array, and then we can do something like pick one key as a signature string and link that up to all unsorted original strings and return values of the dictionaries where sorted strings are keys
        #create a hash map for putting key value, where key is signature and value are list of original strings

        #time complexity o sorting is O(n log n)

        #overall is O(n k log k)
        groups={}
        for string in strs:
            result=sorted(string)
            signature="".join(result)

            if signature in groups:

                groups[signature].append(string)
            else:
                groups[signature]=[string]
        
        return list((groups.values()))

                
            
           




           

        