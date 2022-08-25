import pygame, random

class Cell():
    def __init__(self, x, y, windows, rows, cols):
        self.x = x
        self.y = y
        self.rows = rows
        self.cols = cols
        self.windows = windows
        self.width = 40
        self.walls = [True, True, True, True]
        self.visited = False
        self.tried = False
        self.solutionPart = False

    def findIndex(self, x,y):
        if x < 0 or y < 0 or x > self.rows-1 or y > self.cols -1:
            return False
        else:
            return y * self.cols + x

    def checkNeigbors(self, grid):
        neigbors = []

        top = self.findIndex(self.x,self.y-1)
        right = self.findIndex(self.x+1,self.y)
        bottom = self.findIndex(self.x,self.y+1)
        left = self.findIndex(self.x-1,self.y)

        if top and not grid[top].visited:
            neigbors.append(top)
        if right and not grid[right].visited:
            neigbors.append(right)
        if bottom and not grid[bottom].visited:
            neigbors.append(bottom)
        if left and not grid[left].visited:
            neigbors.append(left)
        
        if len(neigbors) > 0:
            r = random.randint(0,len(neigbors)-1)
            return grid[neigbors[r]]
        else:
            return False

    def removeWall(self, next):
        x =  next.x - self.x
        y =  next.y - self.y
        
        if x == -1:
            self.walls[3] = False
            next.walls[1] = False
        elif x == 1:
            self.walls[1] = False
            next.walls[3] = False
        
        if y == -1:
            self.walls[0] = False
            next.walls[2] = False
        elif y == 1:
            self.walls[2] = False
            next.walls[0] = False

    def checkWallDown(self, grid):
        neigbors = []

        top = self.findIndex(self.x,self.y-1)
        right = self.findIndex(self.x+1,self.y)
        bottom = self.findIndex(self.x,self.y+1)
        left = self.findIndex(self.x-1,self.y)

        if not self.walls[0] and not grid[top].walls[2]:
            neigbors.append(grid[top])
        if not self.walls[1] and not grid[right].walls[3]:
            neigbors.append(grid[right])
        if not self.walls[2] and not grid[bottom].walls[0]:
            neigbors.append(grid[bottom])
        if not self.walls[3] and not grid[left].walls[1]:
            neigbors.append(grid[left])
        
        neigbors = [x for x in neigbors if x.tried == False]
        
        if len(neigbors) > 0:  
            return neigbors
        else:
            return False

    def currentHighlight(self):
        cellx = self.x * self.width
        celly = self.y * self.width 
        pygame.draw.rect(self.windows,(0,255,0), (cellx, celly, self.width, self.width))
        pygame.display.update()

    def currentHighlightSolution(self):
        cellx = self.x * self.width
        celly = self.y * self.width 
        pygame.draw.rect(self.windows,(0,255,255), (cellx, celly, self.width, self.width))
        pygame.display.update()


    def show(self):
        cellx = self.x * self.width
        celly = self.y * self.width 

        if self.visited is True:
            pygame.draw.rect(self.windows,(0,122,0), (cellx, celly, self.width, self.width))
        
        if self.tried is True:
            pygame.draw.rect(self.windows,(122,0,0), (cellx, celly, self.width, self.width))
        
        if self.solutionPart is True:
            pygame.draw.circle(self.windows,(0,0,0), (cellx + self.width/2, celly + self.width/2), 10)


        pygame.draw.line(self.windows,(255,255,255), (cellx, celly), (cellx +self.width, celly)) if self.walls[0] is True else None
        pygame.draw.line(self.windows,(255,255,255), (cellx + self.width, celly), (cellx + self.width, celly + self.width)) if self.walls[1] is True else None
        pygame.draw.line(self.windows,(255,255,255), (cellx + self.width, celly + self.width), (cellx, celly + self.width)) if self.walls[2] is True else None
        pygame.draw.line(self.windows,(255,255,255), (cellx, celly + self.width ), (cellx, celly)) if self.walls[3] is True else None
        pygame.display.update()
       

    def getValue(self):
        return "this x: {0}, this y: {1}, visited: {2}, tried:{4} - wall:  {3}  ".format(self.x, self.y, self.visited, self.walls, self.tried)

    
    
    def __str__(self):
        return f'Cell(this x: {self.x}, this.y: {self.y})'

    def __repr__(self):
        return f'Cell(this x: {self.x}, this.y: {self.y})'
