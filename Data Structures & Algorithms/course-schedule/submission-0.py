class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            hash[crs].append(pre)

        visit=set()
        def dfs(crs):
            if crs in visit:
                return False
            if hash[crs]==[]:
                return True
            
            visit.add(crs)
            for pre in hash[crs]:
                if not dfs(pre): 
                    return False
            visit.remove(crs)
            hash[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False 
        return True


        