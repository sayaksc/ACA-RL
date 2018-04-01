#Grid World Problem
import numpy as np

def nodes(x,y,mat,L): #Find the neighbours
    neighbour=[]
    if (x,y) in L :
        return neighbour
    if x==0 and y==0:
        if (x,y+1) not in L : 
            neighbour.append((x,y+1))
        if (x+1,y) not in L : 
            neighbour.append((x+1,y))
    elif x==0 and y==6 :
        if (x,y-1) not in L : 
            neighbour.append((x,y-1))
        if (x+1,y) not in L : 
            neighbour.append((x+1,y))
    elif x==6 and y==0 :
        if (x,y+1) not in L : 
            neighbour.append((x,y+1))
        if (x-1,y) not in L : 
            neighbour.append((x-1,y))
    elif x==6 and y==6 :
        if (x,y-1) not in L : 
            neighbour.append((x,y-1))
        if (x-1,y) not in L : 
            neighbour.append((x-1,y))
    elif x==0 :
        if (x,y-1) not in L : 
            neighbour.append((x,y-1))
        if (x,y+1) not in L : 
            neighbour.append((x,y+1))
        if (x+1,y) not in L :
            neighbour.append((x+1,y))
    elif x==6 :
        if (x,y-1) not in L : 
            neighbour.append((x,y-1))
        if (x,y+1) not in L : 
            neighbour.append((x,y+1))
        if (x-1,y) not in L :
            neighbour.append((x-1,y)) 
    elif y==0 :
        if (x,y+1) not in L : 
            neighbour.append((x,y+1))
        if (x+1,y) not in L : 
            neighbour.append((x+1,y))
        if (x-1,y) not in L :
            neighbour.append((x-1,y))
    elif y==6 :
        if (x,y-1) not in L : 
            neighbour.append((x,y-1))
        if (x+1,y) not in L : 
            neighbour.append((x+1,y))
        if (x-1,y) not in L :
            neighbour.append((x-1,y))
    else :
        pos=(x,y)
        for i in [(1,0),(0,1),(-1,0),(0,-1)]:
            curr=[0,0]
            curr[0]=pos[0]+i[0]
            curr[1]=pos[1]+i[1]
            if (curr[0],curr[1]) not in L:
                neighbour.append((curr[0],curr[1]))
    return neighbour



def rewards(mat,value, K):  #finds the values
#The reward for each step is -1 while the reward of reaching goal is 5
    for x in range(7):
        for y in range(6,-1,-1):
            if (x,y) in K:
                continue
            L=nodes(x,y,mat,K)
            n=len(L)
            if x==6 and y==0 :
                value[y][x] = 50 + 0.6*np.sum([value[L[i][1]][L[i][0]] for i in range(n)] )/n
            else :
                value[y][x] = -1 + 0.6*np.sum([value[L[i][1]][L[i][0]] for i in range(n)] )/n
    return 0


def display(mat):
    for i in range(7):
        for j in range(7):
            print '%.4f' %(mat[i][j]),'  |',
        print
# main
#Takes input of a grid of dimentions 7x7 into a 2D matrix mat[][]

mat = np.zeros((7,7))
v = np.zeros((7,7))
L = [(4,0),(4,1),(4,2),(0,2),(1,2),(0,3),(2,3),(3,3),(3,4),(5,4),(6,4),(2,6),(3,6),(4,6)]
for i in L:
    mat[i[1]][i[0]] = 1
    v[i[1]][i[0]]=-50
print v, '\n\n'
for i in range(1000):
    rewards(mat, v,L)
    print i
    display(v)
    print '\n'

