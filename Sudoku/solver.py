import random

a = [0, 0, 0, 0, 8, 0, 0, 4, 0]
b = [0, 0, 3, 0, 6, 0, 0, 7, 0]
c = [6, 0, 8, 0, 1, 0, 0, 0, 5]

d = [0, 9, 0, 3, 0, 0, 0, 0, 4]
e = [0, 0, 5, 2, 0, 0, 0, 9, 0]
f = [4, 8, 0, 0, 0, 0, 0, 0, 0]

g = [0, 0, 6, 7, 0, 0, 0, 5, 0]
h = [0, 0, 9, 0, 3, 0, 1, 0, 0]
i = [0, 0, 0, 0, 0, 0, 0, 0, 0]

gridTest = [a, b, c, d, e, f, g, h, i]


# 1-Récuperation des indices des cases vides (emptyIndexRow)
# 2-Récupération des valeurs déjà entrées dans une ligne (enteredValuesRow)
# 3-Récupération des valeurs manquantes d'une ligne (missingValuesRow)
# 4-Assignation des valeurs manquantes sous forme de tableau aux indices des cases vides

# Retourne l'index où les valeurs sont vides (=0)
def emptyIndexRow(row):
    emptyIndex = []
    for i in range(0, len(row)):
        if row[i] == 0 or isinstance(row[i], list):
            emptyIndex.append(i)
    return emptyIndex


def missingValues(row):
    missing = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in row:
        if i != 0 and not isinstance(i, list):
            missing.remove(i)
    return missing


# Retourne les valeurs déjà entrées dans une line
def enteredValuesRow(row):
    values = []
    for i in row:
        if i != 0 and not isinstance(i, list):
            values.append(i)
    return values


def inputPossibilities(grid):
    for row in range(0, len(grid)):
        for val in range(0, len(grid[row])):
            if grid[row][val] == 0:
                grid[row][val] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return grid


# Assigne les possibilités aux index vides
def reducePossibilities(grid):
    # ! Attention ! Ecrire : grid = inputPossibilities(grid) lors de la première utilisation
    for row in range(0, len(grid)):
        similarEnteredValues = False
        while not similarEnteredValues:
            enteredValues = enteredValuesRow(grid[row])
            for val in range(0, len(grid[row])):
                if isinstance(grid[row][val], list):
                    for subVal in grid[row][val]:
                        if subVal in enteredValues:
                            grid[row][val].remove(subVal)
                        if len(grid[row][val]) == 1:
                            grid[row][val] = grid[row][val][0]
            for i in missingValues(grid[row]):
                time = 0
                for k in grid[row]:
                    if isinstance(k,list):
                        if i in k:
                            time+=1
                            indice = grid[row].index(k)
                if time == 1:
                    grid[row][indice] = i
            if enteredValues == enteredValuesRow(grid[row]):
                similarEnteredValues = True



    return grid


# Remet la grille dans son format (après avoir modifié les colonnes)
def columnInRow(grid):
    gridColumn = [[], [], [], [], [], [], [], [], []]
    for row in grid:
        for i in range(0, len(row)):
            gridColumn[i].append(row[i])
    return gridColumn


# Met les colonnes en lignes
def returnToColumn(gridColumn):
    grid = [[], [], [], [], [], [], [], [], []]
    for row in gridColumn:
        for i in range(0, len(row)):
            grid[i].append(row[i])
    return grid


# Met le format grid sous format carre
def gridToSquareFormat(grid):
    gridSquare = [[], [], [], [], [], [], [], [], []]
    for row in range(0, len(grid)):
        # Ligne 1 à 3
        if row < 3:
            for i in range(0, len(grid[row])):
                # i//3 sépare la ligne en 3 tranches et place dans la ligne 1 la tranche 1 , dans la ligne 2 la tranche 2 etc...
                gridSquare[i // 3].append(grid[row][i])
        # Ligne 4 à 6
        elif row < 6:
            for i in range(0, len(grid[row])):
                # le +3 pour atteindre les lignes à l'index 3,4 et 5
                gridSquare[(i // 3) + 3].append(grid[row][i])
        # Ligne 7 à 9
        else:
            for i in range(0, len(grid[row])):
                gridSquare[(i // 3) + 6].append(grid[row][i])
    return gridSquare


# Met le format carre sous format grid
def squareToGridFormat(gridSquare):
    grid = [[], [], [], [], [], [], [], [], []]
    for row in range(0, len(gridSquare)):
        if row < 3:
            for i in range(0, len(gridSquare[row])):
                # Place
                grid[i // 3].append(gridSquare[row][i])
        elif row < 6:
            for i in range(0, len(gridSquare[row])):
                grid[(i // 3) + 3].append(gridSquare[row][i])
        else:
            for i in range(0, len(gridSquare[row])):
                grid[(i // 3) + 6].append(gridSquare[row][i])
    return grid


def filledGrid(grid):
    filled = True
    for row in grid:
        for val in row:
            if val == 0 or isinstance(val, list):
                filled = False
                break
    return filled

def sumList(row):
    sum = 0
    for i in row:
        sum+=i
    return sum

def trueGrid(grid):
    if not filledGrid(grid):
        return False
    else:
        for row in grid:
            if sumList(row)==45:
                return False
        return True


def solver(grid):
    grid = inputPossibilities(grid)
    i = 0
    while i < 100 and not filledGrid(grid):
        grid = reducePossibilities(grid)
        squareGrid = gridToSquareFormat(grid)
        grid = squareToGridFormat(reducePossibilities(squareGrid))
        columnGrid = columnInRow(grid)
        grid = returnToColumn(reducePossibilities(columnGrid))
        i += 1

    return grid


def solverTest(grid):
    grid = inputPossibilities(grid)
    i = 0
    while i < 100 and not filledGrid(grid):
        grid = reducePossibilities(grid)
        squareGrid = gridToSquareFormat(grid)
        grid = squareToGridFormat(reducePossibilities(squareGrid))
        columnGrid = columnInRow(grid)
        grid = returnToColumn(reducePossibilities(columnGrid))
        i += 1
    if not filledGrid(grid):
        if isinstance(grid[4][5],list):
            possibility = grid[4][5]
            for i in possibility:
                grid[4][5] = i



    return grid

print(solverTest(gridTest))
# print(columnInRow(gridTest))
# print(returnToColumn(columnInRow(gridTest)))
# print(solver(gridTest))
# print(gridToSquareFormat(gridTest))
# print(squareToGridFormat(gridToSquareFormat(gridTest)))
# print(inputPossibilityRow(a))
# print(inputPossibilityRow(b))
# print(inputPossibilityRow(c))

# Retourne pour chaque index de valeurs vides
"""
[
[[1, 2, 5, 7, 9],[1, 2, 5, 7], [1, 2, 7], [5, 9], 8, [2, 3, 5, 7, 9], [2, 3, 6, 9], 4, [1, 2, 3, 6, 9]], 
[[1, 2, 5, 9],[1, 2, 4, 5], 3, [4, 5, 9], 6, [2, 4, 5, 9], [2, 8, 9], 7, [1, 2, 8, 9]], 
[6,[2, 4, 7], 8, [4, 9], 1, [2, 3, 4, 7, 9], [2, 3, 9], [2, 3], 5],
 
[[1, 2, 7], 9, [1, 2, 7], 3, [5, 7], [1, 5, 6, 7, 8], [2, 5, 6, 7, 8], [1, 2, 6, 8], 4],
[3, 6, 5, 2, 4, [1, 7, 8], [7, 8], 9, [1, 7, 8]], 
[4, 8, [1, 2, 7], [1, 5, 6, 9], [5, 7, 9], [1, 5, 6, 7, 9], [2, 3, 5, 6, 7], [1, 2, 3, 6], [1, 2, 3, 6, 7]],

[[1, 2, 8], [1, 2, 3], 6, 7, [2, 9], [1, 2, 8, 9], 4, 5, [2, 3, 8, 9]], 
[[2, 5, 7, 8], [2, 5, 7], 9, [4, 5, 6, 8], 3, [2, 4, 5, 6, 8], 1, [2, 6, 8], [2, 6, 7, 8]],
[[1, 2, 5, 7, 8], [1, 2, 3, 5, 7], 4, [1, 5, 6, 8, 9], [2, 5, 9], [1, 2, 5, 6, 8, 9], [2, 3, 6, 7, 8, 9], [2, 3, 6, 8], [2, 3, 6, 7, 8, 9]] 
]

"""
