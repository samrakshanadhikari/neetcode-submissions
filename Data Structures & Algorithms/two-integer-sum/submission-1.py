class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i, num in enumerate(nums):

            complement=target-num
            if complement not in dict:

                dict[num]=i #store key as num and value as index i
            else:
                return[dict[complement],i]
            
                
        

        

            
        


        




        