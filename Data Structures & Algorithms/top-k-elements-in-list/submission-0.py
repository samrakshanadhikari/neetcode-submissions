class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first make a dictionary to map numbers and frequency
        freq={}
        for num in nums: #big O(n)
            if num in freq:
                freq[num]+=1 #big O 1
            else:
                freq[num]=1
            
        #NOw we have a hash map
        #Now we can create a bucket list
        bucket=[[]for _ in range(len(nums)+1)]
        #index=frequency
        #Now store the index and map to list of numbers in the buckets
        for num, frequency in freq.items(): #same big O n
            bucket[frequency].append(num) #constant time
        #store the list of numbers in the list
        result=[]

        #Now, we have frequency and mapping to list of numbers, now we want to return the list of most frquent k number
        for index in range(len(bucket)-1,0,-1): #big O n
            for num in bucket[index]: #this one in worst case what will happen is one number/ value has large frequency, so again big O(n), so overall time complexity would be big O(n^2)?
                result.append(num)
                if len(result)==k:
                    return result
         
                
            #otherwise go back to loop 
                

            

        
            




        