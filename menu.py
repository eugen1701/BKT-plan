#CONSTANTS:
NUMBER_DIRECTIONS = 8
NUMBER_OF_THE_UPPERLEFT_EDGE = 0
NUMBER_OF_THE_LOWERRIGHT_EDGE = 9 #because python I cannot set it in main :)
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

#DECLARATION:
matrice = []
matrice2 = []
#matrice is for the data we read and  matrice2 is for computing the paths, the results
n = 0
xp = 0
yp = 0
#xp and yp are the initial position of the P (paznic)

#PROCEDURES:
def bune(i, j):
    return i>=NUMBER_OF_THE_UPPERLEFT_EDGE and i<=NUMBER_OF_THE_LOWERRIGHT_EDGE and j>=NUMBER_OF_THE_UPPERLEFT_EDGE and j<=NUMBER_OF_THE_LOWERRIGHT_EDGE

def solutie(i, j):
    return i == NUMBER_OF_THE_UPPERLEFT_EDGE or j == NUMBER_OF_THE_UPPERLEFT_EDGE or i == NUMBER_OF_THE_LOWERRIGHT_EDGE or j == NUMBER_OF_THE_LOWERRIGHT_EDGE
    #it is a solution when the coordonates are on the edge of the matrix

def afis():
    for i in range(10):
        print(matrice2[i])
    print("\n")
    print("\n")
    print("\n")

def bkt(pas, i , j):
    for k in range(NUMBER_DIRECTIONS):
        ii = i + di[k]
        jj = j + dj[k]
        if bune(ii, jj):
            if matrice[ii][jj] == 0 and matrice2[ii][jj] == 0:
                matrice2[ii][jj] = pas
                if solutie(ii, jj):
                    afis()
                    matrice[ii][jj] = -1 # infinit loop but why? BUG ---> solved
                    matrice2[ii][jj] = 0# because I was putting 0 it was following always the same path
                    break
                bkt(pas+1, ii, jj)
                matrice2[ii][jj]=0 # It puts zero when it reverse

#MAIN:
def main():
    file_object = open("data.txt", "r")
    stuff = file_object.readlines()
    n = int(stuff[0])
    NUMBER_OF_THE_LOWERRIGHT_EDGES = n-1

    for i in range(n):
        line = []
        for j in range(n):
            line.append(0)
        matrice.append(line)

    stuff = stuff[1:]
    for i in range(n):
        for j in range(n):
            try:
                if stuff[i][j] == "x" :
                    matrice[i][j] = -1
                elif stuff[i][j] == "P":
                    matrice[i][j] = 1
                    xp = i
                    yp = j
            except:
                break

    for i in range(n):
        line = []
        for j in range(n):
            if i == xp and j == yp:
                line.append(1)
            else:
                line.append(0)
        matrice2.append(line)
    bkt(2, xp, yp)


main()