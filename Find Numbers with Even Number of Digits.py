class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            j=str(i)
            x=len(j)
            if x%2==0:
                c=c+1
        return c
