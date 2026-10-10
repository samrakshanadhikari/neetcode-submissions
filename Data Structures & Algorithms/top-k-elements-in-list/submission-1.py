class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for num in nums:
            if num not in dict:
                dict[num]=1
            else:
                dict[num]+=1
        sorted_nums= sorted(dict, key=dict.get,reverse=True)
        result= sorted_nums[:k]

        return result
    


        