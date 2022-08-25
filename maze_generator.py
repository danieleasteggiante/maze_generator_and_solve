from re import I, S
import pygame
import sys
import math
from Cell import Cell

BLACK = (25, 25, 25)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))   
window.fill(BLACK)
pygame.init()

CLOCK = pygame.time.Clock()
w = 40
grid = []
stack = []


current=None

def setup():
    global window, current, CLOCK
    cols = math.floor(400/w)
    rows = math.floor(400/w)
    for j in range(0, rows):
        for i in range(0, cols):
            cell = Cell(i,j,window, rows, cols)
            grid.append(cell)
    current = grid[0]
    current.visited = True


def display_grid():
    global CLOCK
    CLOCK.tick(60)
    for i in range(0, len(grid)):
        grid[i].show()


def resolve(current, solution =[], position_saved = []):
    global grid, CLOCK
    
    display_grid()
    
    solution.append(current)
    current.tried = True
    current.currentHighlightSolution()
    
    if current and current.x == 9 and current.y == 9:
        indexFrom = []
        for pos in position_saved:
            print(pos)
            print(len(pos[1]))
            if len(pos[1]) > 1 and len(pos[1]) < 3:
                if pos[1][0] in solution and pos[1][1] in solution:
                    index = [solution.index(pos[1][0]), solution.index(pos[1][1])]
                    for i in index:
                        print(i)
                        indexFrom.append(i)

            elif len(pos[1]) > 2 and len(pos[1]) < 4:
                print('Errore')
           
            else:
                print('non ce')

        print('resolved')
        solutionDef = []
        toSlice =[]
        toSlice.append(0)
        bigger = 0
        for i in range(0,len(indexFrom)):
            if indexFrom[i] > bigger:
                bigger = indexFrom[i]
                toSlice.append(indexFrom[i])
        
        print(toSlice)
        if len(toSlice) > 0:
            for i in range(0, len(toSlice)-1,2):
                solutionDef = solutionDef + solution[toSlice[i]:toSlice[i+1]]
            solutionDef = solutionDef + solution[toSlice[-1]:]
                

        else:
            solutionDef = solution
        print(solutionDef)
        for i in solutionDef:
            i.solutionPart = True
        return solution 
    
    next = current.checkWallDown(grid)
        
    if next and len(next) == 1:
        current = next[0]
        resolve(current, solution)

    elif next and len(next) > 1:
        position_saved.append([current, [x for x in next]])
        for i in next:
            if i.tried==False:
                resolve(i, solution)
    else:
        print('fine branch')
                   
                             
def draw():
    global current, window, CLOCK, stack, grid
    while True:
        display_grid()
        next = current.checkNeigbors(grid)
        if next:
            stack.append(current)
            current.removeWall(next)
            current.currentHighlight()
            next.visited = True
            current = next
        elif len(stack) > 0:
            current = stack.pop()
            current.currentHighlight()
        elif len(stack) < 1:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
setup()
draw()
resolve(grid[0])

while True:
    display_grid()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()





    

