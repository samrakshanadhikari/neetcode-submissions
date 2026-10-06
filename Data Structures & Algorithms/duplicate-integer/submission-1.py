class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        if nums==[]:
            return False   
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        
        return False


        