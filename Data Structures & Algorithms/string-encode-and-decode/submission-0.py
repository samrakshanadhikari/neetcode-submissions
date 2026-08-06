class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for string in strs:
            result+= str(len(string))+"#" +string

        return result


    def decode(self, s: str) -> List[str]:
        i=0
        
        result=[]
        while i< len(s):
            j=i
            while s[j]!="#":
                j=j+1
            length=int(s[i:j])
            #slice
            word=s[j+1:j+1+length]
            result.append(word)
            i=j+1+length
            
        return result

        


        #do something like go thouh each charcater, initialize i=0 and j=i+1 move j and when you find j="#", you have to pause and conclude that lenght of the first string is len(j-i), and then append the rest of string up to length len(j-i) into the list and now go on moving j and when it finds again "#", repeat same thing, this is how you can decode
        
            

