from collections import defaultdict
class Solution:
    def alien_order(self, words):
        

        #self.output
        self.output =[]
        self.visited =set()
        self.record = []


        # construct our adjSet
        self.adjSet = {char: set() for word in words for char in word}
        for i in range(len(words)-1):
            firstWord = words[i]
            secondWord = words[i+1]

            minLength = min(len(firstWord),len(secondWord))

            if len(firstWord)>len(secondWord) and firstWord[:minLength] == secondWord[:minLength]:
                return ""
            
            for j in range(minLength):
                if firstWord[j]!=secondWord[j]:
                    self.adjSet[firstWord[j]].add(secondWord[j])
                    break

        # run all nodes
        for char in sorted(self.adjSet.keys(),reverse=True):
            if not self.dfs_postorder(char):
                return ""

        self.output.reverse()
        return "".join(self.output)

    def dfs_postorder(self,char):
        # base case
        if char in self.visited:
            return False
        if char in self.record:
            return True
        
        self.visited.add(char)

        for next in self.adjSet[char]:
            if not self.dfs_postorder(next):
                return False

        self.output.append(char)
        self.record.append(char)
        self.visited.remove(char)
        return True

