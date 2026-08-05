class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for index, num in enumerate(nums):
            complementary=target-num
            if complementary in hash:
                return([hash[complementary],index])
                
            hash[num]=index

        

            




        