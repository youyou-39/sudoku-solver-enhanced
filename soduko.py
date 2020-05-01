from copy import deepcopy
complexity = 0
class cell:
    def __init__(self):
        self.possibilies = [True for i in range(9)]
        self.count = 9
        self.val = 0
    
    def set(self , val ):
        self.val = val
        self.count = 1
        self.possibilies = [False for i in range(9)]
        # print("set to" , val)

    def isSet(self)-> bool:
        if self.count == 1:
            return True
        else:
            return False

    def removePossibility( self , val ) -> bool:
        if self.possibilies[val-1]:
            self.possibilies[val-1] = False
            self.count -= 1
            if self.isSet():
                for i in range(9):
                    if self.possibilies[i]:
                        self.set(i+1)
            return True
        return False

class matrix:
    def __init__(self,grid):       
        self.currentcell = [0,0]
        self.lefwega3tany = False
        self.grid = grid
        self.cells = [[cell()for x in range( 9 )]for y in range(9)]
        for x in range(9):
            for y in range(9):
                if self.grid[x][y]:
                    self.cells[x][y].set(self.grid[x][y]) 
                    

    def getQuadrent(self, valx , valy ):
        return (valx//3 , valy//3)

    
    def removePossibilityQuadrent(self, x,y,val)->bool:
        ret = False
        count = 0
        for i in range(x*3 , x*3+3 ):
            for j in range( y*3 , y*3+3 ): 
                ret |= self.cells[i][j].removePossibility(val)
                
                if self.cells[i][j].val == val:
                    count += 1
                    if count > 1:
                        self.lefwega3tany = True
        return ret

    def loop(self):
        change = True
        while change:
            global complexity 
            complexity +=1
            change = False
            for i in range(9):
                for j in range(9):
                    if self.cells[i][j].isSet():
                        val = self.cells[i][j].val
                        for k in range(9):
                            if self.cells[i][k].val == val and j != k:
                                self.lefwega3tany = True
                            change |= self.cells[i][k].removePossibility(val)
                            
                        for k in range(9):
                            if self.cells[k][j].val == val and i != k:
                                self.lefwega3tany = True
                            change |= self.cells[k][j].removePossibility(val)
                        (x,y) = self.getQuadrent(i,j)
                        change |= self.removePossibilityQuadrent(x,y,val)
                    else:
                        pass
                        # print(i,j,self.cells[i][j].possibilies)

    def get_next_empty_cell(self):
        for self.currentcell[0] in range(self.currentcell[0] , 9):
            for self.currentcell[1] in range(self.currentcell[1] , 9):
                if not self.cells[self.currentcell[0]][self.currentcell[1]].isSet():
                    return True
        return False

    def backtracking(self):
        global complexity
        complexity += 1
        m  =  matrix([[0 for i in range(9)]for j in range(9)])
        m.cells = deepcopy(self.cells)
        if m.get_next_empty_cell():
            isMessedup = True
            for i in range(9):
                if m.cells[m.currentcell[0]][m.currentcell[1]].possibilies[i]:
                    temp = deepcopy(m)
                    temp.cells[m.currentcell[0]][m.currentcell[1]].set(i+1)
                    temp.loop()
                    if temp.lefwega3tany : 
                        continue
                    isMessedup = False 
                    if temp.backtracking():
                        self.cells = temp.cells
                        # m.cells = temp.cells
                        return True                  
            if isMessedup:
                return False 
        else:
            self.cells = m.cells
            return True
    


    def print_grid(self): 
        for i in range(9): 
            for j in range(9):  
                print (self.cells[i][j].val , " ",end='')
            print()
            
    

grid = [[3,0,6,5,0,8,4,0,0], 
        [5,2,0,0,0,0,0,0,0], 
        [0,8,7,0,0,0,0,3,1], 
        [0,0,3,0,1,0,0,8,0], 
        [9,0,0,8,6,3,0,0,5], 
        [0,5,0,0,9,0,6,0,0], 
        [1,3,0,0,0,0,2,5,0], 
        [0,0,0,0,0,0,0,7,4], 
        [0,0,5,2,0,6,3,0,0]] 

m = matrix(grid)
m.loop()
m.backtracking()
m.print_grid()
print("practical complexity of enhanced backtracking = " + str(complexity) + " n*n : n being 9")