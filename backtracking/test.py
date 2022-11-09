class Solution:
    def __init__(self):
        self.b='world'

    def hi(self):
        self.a ='hi'

    def printtest(self):
        print(self.a)

s =Solution()
s.printtest()

from collections import Counter
from collections import defaultdict
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
count = defaultdict(int, sum(map(Counter, board), Counter()))
print(count)