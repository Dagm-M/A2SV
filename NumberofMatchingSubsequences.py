class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.count = 0
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        current_node = self.root
        for character in word:
            current_node = current_node.children.setdefault(character, TrieNode())
        current_node.is_word = True
        current_node.count += 1
        
    def search(self,word):
        curr= self.root
        ans = 0
        def dfs(node, index):
            nonlocal ans
            for char in node.children:
                for i in range(index, len(word)):
                    if word[i] == char:
                        ans += node.children[char].count
                        dfs(node.children[char], i + 1)
                        break
        
        dfs(curr,0)
        return ans

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        wordDictionary = WordDictionary()
        for word in words:
            wordDictionary.addWord(word)

        return wordDictionary.search(s)
