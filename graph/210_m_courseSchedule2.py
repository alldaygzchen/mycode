class Solution:
    def findOrder(self, numCourses, prerequisites):

        # init
        # create record for visited to prevent TLE
        self.numCourses = numCourses
        self.prerequisites = prerequisites
        self.output = []
        self.record = []
        
        # create adjacent list of each course
        self.adjList = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            self.adjList[crs].append(pre)

        # use dfs postorder to run each course
        for c in range(self.numCourses):
            if not self.dfs_postorder(c,set()):
                return []

        # return the topological sort
        return self.output
        

    # params: visit and current course
    # output: true or false but add new course to record
    def dfs_postorder(self,crs,visit):

        #base case
        if crs in visit:
            return False
        if crs in self.record: #if self.adjList[crs] == [] still runs
            return True

        #formula
        visit.add(crs)
        for pre in self.adjList[crs]:
            if not self.dfs_postorder(pre,visit):
                return False
        self.record.append(crs)
        self.output.append(crs)
        visit.remove(crs)
        return True