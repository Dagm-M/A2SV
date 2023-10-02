class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.val = 0
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word, val):
        current_node = self.root
        for character in word:
            current_node = current_node.children.setdefault(character, TrieNode())
            current_node.val += val
        current_node.is_word = True
        
    def search(self, word):
        curr= self.root
        res = 0
        for char in word:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
            res = curr.val

        return res

class MapSum:

    def __init__(self):
        self.wordDictionary = WordDictionary()
        self.seen = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        if key in self.seen:
            self.wordDictionary.addWord(key,val - self.seen[key])
        else:
            self.wordDictionary.addWord(key,val)
        self.seen[key] = val

    def sum(self, prefix: str) -> int:
        return self.wordDictionary.search(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
