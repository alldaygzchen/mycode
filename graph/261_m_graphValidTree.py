class Solution:
    """
    @param n: n nodes labeled as 0 ~ n-1 nodes
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):

        # init
        # create adjList and  it is undirected
        self.adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            self.adj[n1].append(n2)
            self.adj[n2].append(n1)

        # create visit to prevent duplicate
        self.visit = set()

        # dfs preorder => whether current node is visited

        # run at a random point
        #check it is cycled or not a graph valid Tree
        if self.dfs_preorder(0,-1) and len(self.visit) == n:
            return True
        return False
        
    def dfs_preorder(self,curr,prev):
        if curr in self.visit:
            return False

        self.visit.add(curr)

        for j in self.adj[curr]:
            
            if j==prev:
                continue
    
            if not self.dfs_preorder(j,curr):
                return False

        return True
            