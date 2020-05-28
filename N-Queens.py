#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # initialize a positions board of columns
        pos = [-1]*n
        row = 0
        sol = []
        self.solve(pos, row, sol)
        return sol
    
    def solve(self, pos: List[int], row: int, sol: List[List[str]]):
        n = len(pos)
        if row==n:
            sol.append(self.createList(pos))
            return
        for col in range(n):
            if self.isValid(pos,row,col):
                pos[row] = col
                self.solve(pos,row+1,sol)
                pos[row] = -1
    
    def createList(self, pos: List[int]) -> List[str]:
        result = []
        n = len(pos)
        for i in range(n):
            temp = "." * n
            p = pos[i]
            result.append(temp[:p] + 'Q' + temp[p+1:])
        return result
    
    def isValid(self, pos: List[int], row: int, col: int) -> bool:
        for i in range(row):
            # checks if queen is in its own column, row
            if pos[i] == col or abs(row - i) == abs(col - pos[i]):
                return False
        return True

