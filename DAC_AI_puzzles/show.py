import os

RED = '\033[41m'
GREEN = '\033[42m'
NC = '\033[0m'
WHITE = '\033[47m'
BLUE = '\033[44m'
YELLOW = '\033[43m'

def printMat(mat):
    
    #os.system('clear')
    d1 = 'tput cup '
    d2 = ' 35'
    i = 8
    for row in mat:
        s = ""
        d = d1 + str(i) + d2
        os.system(d)
        for x in row:
            if x == '#':
                s += RED + '  ' + NC
            elif x == '.':
                s += WHITE + '  ' + NC
            elif x == 'x':
                s += BLUE + '  ' + NC
            elif x == 's':
                s += GREEN + '  ' + NC
            elif x == 'e':
                s += GREEN + '  ' + NC
            elif x == 'a':
                s += YELLOW + '  ' + NC
        print(s)
        i += 1

    os.system('sleep 0.1')
