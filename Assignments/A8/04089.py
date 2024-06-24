# 04089:电话号码

class Node:
    def __init__(self, is_root=False, key=None):
        if not is_root:
            self.key = key
        self.children = {}
        self.is_end_of_word = 0
    
    def add_char(self, char):
        if char not in self.children:
            self.children[char] = Node(key=char)
        return self.children[char]
    
    def end_of_word(self):
        self.is_end_of_word += 1

class Trie:
    def __init__(self):
        self.root_node = Node(is_root=True)
        self.words = {}
    
    def add_word(self, word):
        node_now = self.root_node
        for char in word:
            node_now = node_now.add_char(char)
        node_now.end_of_word()
        self.words[word] = node_now
    
    def is_consistent(self):
        for word in self.words.values():
            if (word.is_end_of_word == 1 and word.children != {}) or word.is_end_of_word > 1:
                return False
        return True

t = int(input())
for _ in range(t):
    trie = Trie()
    n = int(input())
    for _ in range(n):
        trie.add_word(input())
    print("YES" if trie.is_consistent() else "NO")
