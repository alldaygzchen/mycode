from collections import defaultdict
#not done

class Solution:
    def alienOrder(self, words):
        
        #prevent duplicate
        self.visited =set()

        #self.record
        self.record =[]


        # construct our adjSet
        self.adjSet = defaultdict(set)
        for i in range(len(words)-1):
            firstWord = words[i]
            secondWord = words[i]

            minLength = min(len(firstWord),len(secondWord ))

            if len(firstWord)>len(secondWord) and firstWord[:minLength] == secondWord[:minLength]:
                return ""
            else:
                for j in len(minLength):
                    if firstWord[j]!=secondWord[j]:
                        self.adjSet[firstWord[j]].add(secondWord[j])
                        break

        # run all nodes
        for char in self.adjSet:
            if not self.dfs_postorder(char):
                return False

        self.res.reverse()
        return "".join(self.res.reverse())

    def dfs_postorder(self,char):
        # base case
        if char in self.visit:
            return False
        
        self.visited.add(char)

        for next in self.adjSet[char]:
            if not self.dfs_postorder(next):
                return False

        self.record.append(char)
        self.visited.remove(char)
        return True

        

        