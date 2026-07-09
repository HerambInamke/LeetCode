class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], D: int, q: List[List[int]]) -> List[bool]:
        C=[i:=0]+[i:=i+(prev+D<x) for prev, x in pairwise(nums)]
        return [C[x]==C[y]for x, y in q]
        