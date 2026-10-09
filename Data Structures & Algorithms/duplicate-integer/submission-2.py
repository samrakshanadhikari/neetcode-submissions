class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # have to return true if any duplicates otheriwse return false
        #to see duplicates we can use Set which tracks numbers you have already seen
        seen= set()
        for num in nums: 
            if num not in seen:

                seen.add(num)
            else:
                return True

        return False

        