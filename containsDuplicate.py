from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False 
         

solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 3]))  # Should print True
print(solution.hasDuplicate([1, 2, 3, 4]))  # Should print False

