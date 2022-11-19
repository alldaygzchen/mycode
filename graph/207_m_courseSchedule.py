# input is an array
# DFS postorder

# Steps: 
# Create a vertex adjacent list
# Use dfs postorder to check whether the course is prequire
    # params: the current course,path
    #if the course can be completed marked as [] prevent TLE
# loop every course if has False return False 



class Solution:
    def canFinish(self,numCourse,prerequisites):

        # Create a vertex adjacent list

        self.numCourse = numCourse
        self.adjList = {i:[] for i in range(self.numCourse)}
        for course ,pre in prerequisites:
            self.adjList[course].append(pre)
        

        # loop every course if has False return False

        for c in range(numCourse):
            if not self.dfs_postorder(c,set()):
                return False
        return True

    # Use dfs postorder to check whether the course is prequire
    def dfs_postorder(self,course,visit):
        
        if course in visit:
            return False
        if self.adjList[course] == []:
            return True

        visit.add(course)

        for pre in self.adjList[course]:
            if not self.dfs_postorder(pre,visit):
                return False
        
        visit.remove(course)

        #if the course can be completed marked as [] prevent TLE
        self.adjList[course] = []

        return True



