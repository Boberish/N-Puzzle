import sys
import cProfile
import heapq as heap


#######globals:
final_puzzle = []
size = 0
idx_dic = {}


# final_puzzle = ((1,2,3),(8,0,4),(7,6,5))
# final_puzzle = ((1,2,3,4),(12,13,14,5),(11,0,15,6), (10,9,8,7))

def make_goal():
    global size
    # print(size)
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

def swap(puz, og_x, og_y, x, y):
    global size
    if x < 0 or y < 0 or x == size or y == size:
        return 0
    new = list(list(line) for line in puz)
    new[og_x][og_y] = puz[x][y]
    new[x][y] = 0
    return tuple(tuple(line) for line in new)

def swapWithNb(puz, og_x, og_y, x, y, nb):
    global size
    if x < 0 or y < 0 or x == size or y == size:
        return 0
    new = list(list(line) for line in puz)
    new[og_x][og_y] = puz[x][y]
    new[x][y] = nb
    return tuple(tuple(line) for line in new)


def find_neighbors(puz):
    x, y = index_2d(0, puz)
    u = swap(puz, x, y, x, y + 1)
    r = swap(puz, x, y, x - 1, y)
    d = swap(puz, x, y, x, y - 1)
    l = swap(puz, x, y, x + 1, y)
    return [e for e in [u,r,d,l] if e]

def index_2d(search, data):
    for i, e in enumerate(data):
        try:
            return i, e.index(search)
        except ValueError:
            pass

def make_lookup_dic_heru():
    global size
    global final_puzzle
    dic = {}
    for num in range(size * size):
        dic[num] = index_2d(num, final_puzzle)
    return(dic)


def h_cost(puzzle):
    global size
    global idx_dic
    if (str(sys.argv[2]) == "mp"):
        return (misplaced(puzzle))
    if (str(sys.argv[2]) == "gt"):
        ret = g_thing(puzzle, 0, 0)
        return (ret)
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
    # puz = puz
    new[og_x][og_y] = puz[x][y]
    new[x][y] = 0
    return tuple(tuple(line) for line in new)


def find_neighbors(puz):
    x, y = index_2d(0, puz)
    d = swap(puz, x, y, x, y - 1)
    l = swap(puz, x, y, x + 1, y)
    u = swap(puz, x, y, x, y + 1)
    r = swap(puz, x, y, x - 1, y)
    return [e for e in [u,r,d,l] if e]  


def get_path(cameFrom, current):
    done = []
    done.append(current)
    while current in list(cameFrom.keys()):
        current = cameFrom[current]
        done.append(current)
    return (done)


def misplaced(puzzle):
    global size
    count = 0
    for x in range(size):
        for y in range (size):
            if puzzle[x][y] == final_puzzle[x][y]:
                count += 1
    return (size * size - count)

def g_thing(puzzle, nb, count):
    global idx_dic
    global final_puzzle

    if (puzzle == final_puzzle):
        return (count)
    while(index_2d(nb, puzzle) != index_2d(nb, final_puzzle)):
        x,y = index_2d(nb, puzzle)
        num = final_puzzle[x][y]
        currentX, currentY = index_2d(num, puzzle)
        puzzle = swapWithNb(puzzle, x, y, currentX, currentY, nb)
        count += 1
    return g_thing(puzzle, nb + 1, count)






def opening():
    start = []
    # check correct number of arguments (just one for one file)

    if len(sys.argv) != 3:
        print("problem with args")
        sys.exit(1)

    # open file
    try:
        with open(sys.argv[1], 'r') as puzzle:
            start = (puzzle.read().split("\n"))
    except Exception as e:
        print("problem reading file")
        print("Error info: %s" % e)
        sys.exit(1)
    return (start)

def parsing(start):
    global size
    # remove comments before grid
    start = [line.split() for line in start if line and line[0] != '#']
    # remove comments after numbers, but if # is connected to number it doesnt work
    for line in start:
        for i in range(len(line)):
            if line[i][0] == '#':
                del line[i:]
                break
    # convert numbers into ints
    try:
        start = [list(map(int, lst)) for lst in start]
    except Exception:
        print("problem, puzzle contains non numbers")
        sys.exit(1)
    #remove size from start of start and make it an int
    size = start.pop(0)
    size = size[0]

    #check puzzle y size
    if size != len(start):
        print("error puzzle not correct size")
        sys.exit(1)

    # check puzzle x size
    for line in start:
        if len(line) != size:
            print("error puzzle not correct size")
            sys.exit(1)

    # make list with correct numbers, remove numbers in actual, if anything left over crash
    correct =  list(range(size * size))
    try:
        check = [correct.remove(n) for line in start for n in line]
    except Exception:
        print("FATAL ERROR : not sequentail numbers for size %d" % size)
        sys.exit(1)
    if (len(correct) != 0):
        print("FATAL ERROR : not sequentail numbers for size %d" % size)
        sys.exit(1)
    return(tuple(tuple(line) for line in start))



def init(start):
    global final_puzzle
    global idx_dic
    global size
    realfin = []
    # start = tuple(tuple(line) for line in start)
    final_puzzle = make_goal()
    for line in range(0,size*size,size):
        realfin.append(final_puzzle[line:line + size])
    final_puzzle = tuple(tuple(x) for x in realfin)
    idx_dic = make_lookup_dic_heru()

def slow(que, neigh):
    for i,j in enumerate(que):
        if j[2:] == neigh:
            del que[i]



def doit(start):
    global final_puzzle
    global size
    que = []
    heap.heapify(que)
    closedSet = set()
    openSet = {}
    cameFrom = {}
    openSet[start] = (h_cost(start),0)
    heap.heappush(que, openSet[start] + start )
    dups = {}
    i = 0
    while openSet:
        i += 1
        current = (heap.heappop(que))
        try:
            while dups[current] == 0:
                del dups[current]
                current = (heap.heappop(que))    
        except:
            pass
        curGs = current[1]
        current = current[2:]

        closedSet.add(current)
        del openSet[current]
        
        if current == final_puzzle:
            print("solved in %d iterations" % i)
            path = get_path(cameFrom, current)
            print("steps to solve: %d" % len(path))
            # for puz in path:
            #     for inner in puz:
            #         print(inner)
            #     print("\n",end='')
            sys.exit(0)

        for neigh in find_neighbors(current):
            if neigh in closedSet:
                continue
            tmp_gscore = curGs + 1 # distance from current to neighbor is always 1 here
            if neigh not in openSet:
                openSet[neigh] = ( h_cost(neigh) + tmp_gscore, tmp_gscore)
                heap.heappush(que,(openSet[neigh][0], tmp_gscore) + neigh )

            elif tmp_gscore >= openSet[neigh][1]:
                continue
            else:
                dups[openSet[neigh] + neigh] = 0
                openSet[neigh] = ( h_cost(neigh) + tmp_gscore, tmp_gscore)
                heap.heappush(que,(openSet[neigh][0], tmp_gscore) + neigh)

            cameFrom[neigh] = current
    print("not found")
        

def main():
    start = parsing(opening())
    init(start)
    doit(start)


main()



# arr = (4,1,((1,2,3),(2,3,4)(2,3,4)))






















