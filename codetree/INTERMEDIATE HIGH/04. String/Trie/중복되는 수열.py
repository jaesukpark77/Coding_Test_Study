# problem link : https://www.codetree.ai/missions/9/problems/duplicate-sequence?&utm_source=clipboard&utm_medium=text

n = int(input())
words = [input() for _ in range(n)]

class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(10)]

root = TrieNode()

def insert_word(s):
    t = root
    for char in s:
        index = ord(char) - ord('0')
        if t.children[index] is None:
            t.children[index] = TrieNode()
        
        t = t.children[index]
    t.is_end = True

def search_word(s):
    t = root
    for char in s:
        if t.is_end:
            return True
        
        index = ord(char) - ord('0')
        t = t.children[index]

    return False

for word in words:
    insert_word(word)

exists = False
for word in words:
    if search_word(word):
        exists = True

print(0 if exists else 1)