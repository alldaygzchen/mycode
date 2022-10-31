class TrieNode:

    def __init__(self):
        #root is empty => no value
        self.children = [None]*26
        self.end = False


class Trie:

    def __init__(self):
        
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        curr = self.root
        for w in word:
            i= ord(w)-ord('a')
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            i = ord(w)-ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]

        return curr.end

    def startsWith(self, prefix: str) -> bool:

        curr = self.root
        for p in prefix:
            i = ord(p)-ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]

        return True