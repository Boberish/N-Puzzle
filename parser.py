import sys
import collections
import cProfile

arr = []

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

def h_cost(puzzle):
    score = 0

    for x in range(size):
        for y in range (size):
            real_idx = index_2d(puzzle[x][y], final_puzzle)
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

newArr = ()

newArr = tuple(tuple(line) for line in arr)
final_puzzle = ((1,2,3),(8,0,4),(7,6,5))
# final_puzzle = ((1,2,3,4),(12,13,14,5),(11,0,15,6), (10,9,8,7))
# print(newArr)


closedSet = {}
openSet = collections.OrderedDict()
cameFrom = {}


openSet[newArr] = [0,0]
openSet[newArr][1] = h_cost(newArr)


# print(openSet["small"][0])
# print(openSet)
# print (id(openSet[newArr]))
# closedSet[newArr] = openSet[newArr]
# del openSet[newArr]
# print(closedSet)
# print(id(closedSet[newArr]))

# def sortstuff(x):
#     return x[1][1]

def get_path(cameFrom, current):
    done = []
    done.append(current)
    while current in list(cameFrom.keys()):
        current = cameFrom[current]
        done.append(current)
    return (done)


def doit(start):
    closedSet = {}
    openSet = collections.OrderedDict()
    cameFrom = {}
    openSet[start] = [0,h_cost(start)]
    i = 0
    while len(openSet) > 0:
        # i += 1
        # print(i)
        openSet = collections.OrderedDict(sorted(openSet.items(), key=lambda x: x[1][1]))
        # print(openSet)
        current = openSet.popitem(last=False)
        # print(current[0])
        if current[0] == final_puzzle:
            print("SOLVED IT YOYOYO")
            path = get_path(cameFrom, current[0])
            print("steps to solve: %d" % len(path))
            for puz in path:
                for inner in puz:
                    print(inner)
                    # print("\n")
                print("\n",end='')
            sys.exit(0)

        closedSet[current[0]] = current[1] 
        # print(closedSet)
        # print(current)
        for neigh in find_neighbors(current[0]):
            if neigh in closedSet:
                continue
            tmp_gscore = current[1][0] + 1 # distance from current to neighbor is always 1 here

            if neigh not in openSet:
                openSet[neigh] = [tmp_gscore, h_cost(neigh) + tmp_gscore]
            elif tmp_gscore >= openSet[neigh][0]:
                continue
            cameFrom[neigh] = current[0]
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