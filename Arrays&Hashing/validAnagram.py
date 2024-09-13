class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = set()
        set2 = set()
        list1 = list(s)
        list2 = list(t)

        for n in list1:
            set1.add(n)
        
        for m in list2:
            set2.add(m)

        if set1 == set2:
            return True
        return False




solution = Solution()
print(solution.isAnagram("racecar", "carrace")) # returns true
print(solution.isAnagram("jar", "jam")) # returns false

  
