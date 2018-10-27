import sys
import collections
import cProfile

arr = []
# final_puzzle = ((1,2,3),(8,0,4),(7,6,5))
# final_puzzle = ((1,2,3,4),(12,13,14,5),(11,0,15,6), (10,9,8,7))

def make_goal(size):
	num_tile = size * size
	puzzle = [-1 for i in range(num_tile)]
	cur = 1
	x = 0
	ix = 1
	y = 0
	iy = 0
	while True:
		puzzle[x + y * size] = cur
		if cur == 0:
			break
		cur += 1
		if x + ix == size or x + ix < 0 or (ix != 0 and puzzle[x + ix + y*size] != -1):
			iy = ix
			ix = 0
		elif y + iy == size or y + iy < 0 or (iy != 0 and puzzle[x + (y+iy)*size] != -1):
			ix = -iy
			iy = 0
		x += ix
		y += iy
		if cur == size * size:
			cur = 0

	return puzzle



# check correct number of arguments (just one for one file)
if (len(sys.argv) != 2):
    print("problem with number of args")
    sys.exit(1)

# open file
try:
    with open(sys.argv[1], 'r') as puzzle:
        arr = (puzzle.read().split("\n"))
except Exception as e:
    print("problem reading file")
    print("Error info: %s" % e)
    sys.exit(1)

# remove comments before grid
arr = [line.split() for line in arr if line[0] != '#']
# remove comments after numbers, but if # is connected to number it doesnt work
for line in arr:
    for i in range(len(line)):
        if line[i][0] == '#':
            del line[i:]
            break
# convert numbers into ints
try:
    arr = [list(map(int, lst)) for lst in arr]
except Exception:
    print("problem, puzzle contains non numbers")
    sys.exit(1)
#remove size from start of arr and make it an int
size = arr.pop(0)
size = size[0]

#check puzzle y size
if size != len(arr):
    print("error puzzle not correct size")
    sys.exit(1)

# check puzzle x size
for line in arr:
    if len(line) != size:
        print("error puzzle not correct size")
        sys.exit(1)

# make list with correct numbers, remove numbers in actual, if anything left over crash
correct =  list(range(size * size))
try:
    check = [correct.remove(n) for line in arr for n in line]
except Exception:
    print("FATAL ERROR : not sequentail numbers for size %d" % size)
    sys.exit(1)
if (len(correct) != 0):
    print("FATAL ERROR : not sequentail numbers for size %d" % size)
    sys.exit(1)

# print(arr)
def index_2d(search, data):
    for i, e in enumerate(data):
        try:
            return i, e.index(search)
        except ValueError:
            pass

def make_lookup_dic_heru(size):
    dic = {}
    for num in range(size * size):
        dic[num] = index_2d(num, final_puzzle)
    return(dic)
# make_lookup_dic_heru(3)


def h_cost(puzzle):
    score = 0

    for x in range(size):
        for y in range (size):
            real_idx = idx_dic[puzzle[x][y]]
            score += abs(x - real_idx[0]) + abs(y - real_idx[1])
             
    return(score)

def swap(puz, og_x, og_y, x, y):
    if x < 0 or y < 0 or x == size or y == size:
        return 0
    new = list(list(line) for line in puz)
    new[og_x][og_y] = puz[x][y]
    new[x][y] = 0
    return tuple(tuple(line) for line in new)


def find_neighbors(puz):
    x, y = index_2d(0, puz)
    u = swap(puz, x, y, x, y + 1)
    r = swap(puz, x, y, x - 1, y)
    d = swap(puz, x, y, x, y - 1)
    l = swap(puz, x, y, x + 1, y)
    return [e for e in [u,r,d,l] if e]  

# def not_in_spot(puz):


newArr = ()

newArr = tuple(tuple(line) for line in arr)


def get_path(cameFrom, current):
    done = []
    done.append(current)
    while current in list(cameFrom.keys()):
        current = cameFrom[current]
        done.append(current)
    return (done)

realfin = []
final_puzzle = make_goal(size)
for line in range(0,size*size,size):
    realfin.append(final_puzzle[line:line + size])
final_puzzle = tuple(tuple(x) for x in realfin)
idx_dic = make_lookup_dic_heru(size)



def doit(start):
    closedSet = set()
    openSet = {}
    cameFrom = {}
    openSet[start] = [h_cost(start),0]
    i = 0
    while openSet:
        i += 1
        current = min(openSet, key=(openSet.get))
        curGs = openSet[current][1]
        closedSet.add(current)
        del openSet[current]
        if current == final_puzzle:
            print("solved in %d iterations" % i)
            path = get_path(cameFrom, current)
            print("steps to solve: %d" % len(path))
            for puz in path:
                for inner in puz:
                    print(inner)
                    # print("\n")
                print("\n",end='')
            sys.exit(0)

        for neigh in find_neighbors(current):
            if neigh in closedSet:
                continue
            tmp_gscore = curGs + 1 # distance from current to neighbor is always 1 here
            if neigh not in openSet:
                openSet[neigh] = [ h_cost(neigh) + tmp_gscore, tmp_gscore]
            elif tmp_gscore >= openSet[neigh][1]:
                continue
            cameFrom[neigh] = current
    print("not found")
        


doit(newArr)
    

    


def swap(puz, og_x, og_y, x, y):
    if x < 0 or y < 0 or x == size or y == size:
        return 0
    new = list(list(line) for line in puz)
    new[og_x][og_y] = puz[x][y]
    new[x][y] = 0
    return tuple(tuple(line) for line in new)


def find_neighbors(puz):
    x, y = index_2d(0, puz)
    u = swap(puz, x, y, x, y + 1)
    r = swap(puz, x, y, x - 1, y)
    d = swap(puz, x, y, x, y - 1)
    l = swap(puz, x, y, x + 1, y)
    return [e for e in [u,r,d,l] if e]  



# print(find_neighbors(start))


# find_neighbor(newArr)


    
    
    


















# hold = -1
# for line in arr:
#     for i in range(len(line) - 1):
#         hold = -1
#         for j in range(len(line[i]) - 1):
#             if line[i][j] == '#':
#                 hold = i
#                 break
#         if hold > 0:
#             del line[hold:]