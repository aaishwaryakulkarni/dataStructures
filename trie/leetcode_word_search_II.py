"""
212. Word Search II

Given an m x n board of characters and a list of strings words, return all words on 
the board.

Each word must be constructed from letters of sequentially adjacent cells, where 
adjacent cells are horizontally or vertically neighboring. The same letter cell may 
not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def insertWord(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True

class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        for word in words:
            root.insertWord(word)
        
        rows, cols = len(board), len(board[0])
        result, visited = set(), set()

        def dfs(r, c, cur_node, word):
            if (r < 0 or c < 0 or
            r == rows or c == cols or
            (r, c) in visited or board[r][c] not in cur_node.children):
                return
            
            visited.add((r, c))
            cur_node = cur_node.children[board[r][c]]
            word += board[r][c]

            if cur_node.isEnd:
                result.add(word)

            dfs(r - 1, c, cur_node, word)
            dfs(r + 1, c, cur_node, word)
            dfs(r, c - 1, cur_node, word)
            dfs(r, c + 1, cur_node, word)
            visited.remove((r, c))


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)
    

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

soln = Solution()

print(soln.findWords(board, words))
