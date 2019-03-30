import os
import show
import Queue

def print_mat(a):
    for row in a:
        s = ''
        for x in row:
            s += x
        print(s)
    print('\n')

def BFS(grid, start_r, start_c, end_r, end_c):

    m = len(grid)
    n = len(grid[0])
    path_exists = False
    path_grid = [row[:] for row in grid]
    path = [[None for i in range(n)] for i in range(m)]
    q = Queue.Queue()

    r = start_r
    c = start_c
    q.put((r, c))

    while q.empty() == False:
        r, c = q.get()

        if r-1 >= 0 and (grid[r-1][c] == '.' or grid[r-1][c] == 'e'):
            q.put((r-1, c))
            path[r-1][c] = (r, c)
            grid[r-1][c] = 'x'
            if r-1 == end_r and c == end_c:
                path_exists = True
                break
        if r+1 < m and (grid[r+1][c] == '.' or grid[r+1][c] == 'e'):
            q.put((r+1, c))
            path[r+1][c] = (r, c)
            grid[r+1][c] = 'x'
            if r+1 == end_r and c == end_c:
                path_exists = True
                break
        if c-1 >= 0 and (grid[r][c-1] == '.' or grid[r][c-1] == 'e'):
            q.put((r, c-1))
            path[r][c-1] = (r, c)
            grid[r][c-1] = 'x'
            if r == end_r and c-1 == end_c:
                path_exists = True
                break
        if c+1 < n and (grid[r][c+1] == '.' or grid[r][c+1] == 'e'):
            q.put((r, c+1))
            path[r][c+1] = (r, c)
            grid[r][c+1] = 'x'
            if r == end_r and c+1 == end_c:
                path_exists = True
                break
        
        show.printMat(grid)

       
    if path_exists:
        r = end_r
        c = end_c
        while path[r][c] != None:
            path_grid[r][c] = 'a'
            r, c = path[r][c]
            show.printMat(path_grid)
        path_grid[start_r][start_c] = 's'
        path_grid[end_r][end_c] = 'e'
        show.printMat(path_grid)

def read_grid(file_loc):
	
	with open(file_loc, 'r') as fl:
		
		grid = []
		for line in fl.readlines():
			arr = []
			for x in line:
				if x != '\n':
					arr.append(x)
			grid.append(arr)
	
	start_r = start_c = end_r = end_c = None	
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 's':
				start_r = i
				start_c = j
			elif grid[i][j] == 'e':
				end_r = i
				end_c = j
	return grid, start_r, start_c, end_r, end_c

def main():

    grid, start_r, start_c, end_r, end_c = read_grid('grid')
    os.system('clear')
    BFS(grid, start_r, start_c, end_r, end_c)
if __name__ == '__main__':
    main()
