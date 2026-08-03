class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end  = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                current.children[char] = TrieNode()
                current = current.children[char]
        
        current.is_end = True


    def search(self, word: str) -> bool:
        
        current = self.root

        def dfs(node, index):
            if index == len(word):
                return node.is_end
            
            char  = word[index]

            if char != ".":
                if char not in node.children:
                    return False
                
                return dfs(node.children[char], index+1)
            
            else:
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                    
                return False
        
        return dfs(current, 0)
