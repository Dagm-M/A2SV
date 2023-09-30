class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        current_node = self.root
        for character in word:
            current_node = current_node.children.setdefault(character, TrieNode())
        current_node.is_word = True
        
    def search(self,word):
        curr= self.root
        for char in word:
            if char not in curr.children or not curr.children[char].is_word:
                return False

            curr = curr.children[char]

        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = WordDictionary()
        ans = ""
        words.sort()
        for word in words:
            trie.addWord(word)
    

        for word in words:
            if trie.search(word) and len(word) > len(ans):
                ans = word

        return ans
        
