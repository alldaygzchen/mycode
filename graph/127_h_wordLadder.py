from collections import deque
from collections import defaultdict

class Solution:
    """
    output: shortest transformation sequence #int
    """
    def ladderLength(self, beginWord, endWord, wordList):

        # EDGE CASE
        if endWord not in wordList:
            return 0

        # INIT 
        self.adj_list= defaultdict(list)
        self.quene = deque([beginWord])
        self.visit =set([beginWord])
        self.wordList =wordList
        self.beginWord =beginWord
        self.endWord =endWord
        self.res =1 
        
        # CREATE ADJACENT LIST 
        # undirected
        # key:pattern =>value:word
        self.wordList .append(self.beginWord)
        for word in self.wordList :
            for i in range(len(word)):
                key = word[:i]+"*"+word[i+1:]
                self.adj_list[key].append(word)

        # USE BFS RETURN SHORTEST INT SEQ #add visit var to check
        return self.bfs()

    def bfs(self):
        while self.quene:
            for i in range(len(self.quene)):
                word = self.quene.popleft()
                
                # statements
                if  word == self.endWord:
                    return self.res

                for j in range(len(word)):
                    key = word[:j]+"*"+word[j+1:]
                    for value in self.adj_list[key]:
                        if value in self.visit:
                            continue
                        self.quene.append(value)
                        self.visit.add(value) # prevent duplicate

            self.res +=1
        return 0
