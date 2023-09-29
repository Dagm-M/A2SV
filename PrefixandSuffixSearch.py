class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = 0
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word, i):
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character]
            current_node.index = i
        
    def search(self, word):
        curr= self.root

        for char in word:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
        
        return curr.index


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = WordDictionary()
        for i,word in enumerate(words):
            j = 0
            word = word + "{" + word
            while j <= len(word) // 2:
                self.trie.addWord(word[j:],i)
                j += 1
        
        

    def f(self, pref: str, suff: str) -> int:
        word = suff + "{" + pref
        return self.trie.search(word)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
