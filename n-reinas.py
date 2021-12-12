x = 0

def checkQueens(queens, n, k):
    for i in range(0, k):
        if((queens[i] == queens[k]) or (abs(k - i) == abs(queens[k] - queens[i]))):
            return False
    return True

def NQueens(queens, n, k):
    if(k == n):
        global x
        x = x + 1
        print(f'\nSolución: {x}: ', end="")
        for i in range(0, n):
            print(f'{queens[i]} ', end="")
    else:
        for queens[k] in range(0, n):
            if(checkQueens(queens, n, k)):
                NQueens(queens, n, k+1)


k = 0
amount = int(input('\nIngrese la cantidad de reinas: '))
queens = [-1 for n in range(0, amount)]
NQueens(queens, amount, k)