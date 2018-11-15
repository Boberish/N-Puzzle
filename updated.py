import sys
import cProfile
import heapq as heap
import random

final_puzzle = []
size = 0
idx_dic = {}

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
def check_line2(line, direction, idx):
    global idx_dic
    count = 0
    # for i in range(len(line) - 1):

    for i in range(len(line) - 1):
        for j in range(len(line) - i - 1):
            j += i + 1
            tmp = line[i]
            tmp2 = line[j]
            if line[i] == 0 or line[j] == 0:
                continue
            if direction == 'v':
                if idx_dic[line[i]][1] == idx_dic[line[j]][1] and idx == idx_dic[line[i]][1]:
                    if  idx_dic[line[i]][0] > idx_dic[line[j]][0]:
                        count += 1
            else:
                if idx_dic[line[i]][0] == idx_dic[line[j]][0] and idx == idx_dic[line[i]][0]:
                    if  idx_dic[line[i]][1] > idx_dic[line[j]][1]:
                        count += 1
    # return(0)
    return count * 2
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
    # return(tuple(tuple(line) for line in start))
    return(start)
def flatten(puz):
    a = list(x for y in puz for x in y)
    return(a)
def is_solvable(puz):
    # global idx_dic
    global final_puzzle
    global size
    
    inv = 0
    startidx = [puz.index(line) for line in puz for num in line if num == 0]
    finalidx = [final_puzzle.index(line) for line in final_puzzle for num in line if num == 0]
    g = abs(startidx[0] - finalidx[0])
    g += 1
    a = flatten(puz)
    final = flatten(final_puzzle)
    
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            j += i + 1
            if a[i] == 0 or a[j] == 0:
                continue
            # tmp1 = a[i]
            # tmp2 = a[j]
            if final.index(a[i]) >= final.index(a[j]):
                 inv += 1
    
    if size % 2 != 0:
        if inv % 2 == 0:
            print("solvable")
        else:
            print ("UNSOLVABLE")
            sys.exit(1)
    else:
        if inv % 2 == 0:
            if g % 2 != 0:
                print("solvable")
            else:
                print("UNSOLVABLE")
                sys.exit(1)

        else:
            if g % 2 == 0:
                print("solvable")
            else:
                print("unsolvable")
                sys.exit(1)
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

def str_swap(i,j,puz):
    # print(puz)
    # print(i,j)

    z = puz[i * 2]
    o = puz[j * 2]
    if i > j:
        puz = puz.replace(z,o,1)
        # print("here")
        # print(puz)
        puz = puz.replace(o,z,1)
        # print(puz)
    else:
        puz = puz.replace(o,z,1)
        puz = puz.replace(z,o,1)
    return(puz)
    
def new_neigh(puz):
    # print(puz)
    i = int(puz.find('0') / 2)
    # print ("i: %d"%i)
    ret = []
    if i / size > 0:
        ret.append (str_swap(i,i - size, puz))
    if i / size < size - 1:
        ret.append(str_swap(i,i + size, puz))
    if i % size > 0:
        ret.append(str_swap(i,i - 1, puz))
    if i % size < size - 1:
        ret.append(str_swap(i,i + 1, puz))
    return ret



def h_cost(puzzle):
    global size
    global idx_dic
    # dic = {}
    # print(final_puzzle)
    score = 0
    # sys.exit(1)
    # if (str(sys.argv[2]) == "mp"):
    #     return (misplaced(puzzle))
    # if (str(sys.argv[2]) == "gt"):
    #     ret = g_thing(puzzle, 0, 0)
    realfin = []
    for line in range(0,size*size,size):
        realfin.append(final_puzzle[line:line + size])

    for x in range(size):
        for y in range (size):
            real_idx = idx_dic[puzzle[x][y]]
            score += abs(x - real_idx[0]) + abs(y - real_idx[1])
            # print("tmp =",tmp, "nb = ", puzzle[x][y])    #     return (ret)

    for line in range(0,size*size,size):
        realfin.append(final_puzzle[line:line + size])

    print(puzzle)
    # for num in range(1,size * size):
    #     x,y = idx_dic[num]
    #     row = puzzle.index(str(num)) 
    #     row = row // size
    #     tmp = abs((puzzle.index(str(num)) - size * row) % size - x) + abs(row - y)
    #     score += tmp
    #     print("tmp = ", tmp , "nb =", num)
    # print(score)
    sys.exit(1)
    return(score)

    # return random.randint(0,20)
    # score = 0

    # for x in range(size):
    #     for y in range (size):
    #         real_idx = idx_dic[puzzle[x][y]]
    #         score += abs(x - real_idx[0]) + abs(y - real_idx[1])
    # return(score)
    # return(score + lineByline(puzzle))

# def str_hcost(puz):
    

def swap(puz, og_x, og_y, x, y):
    if x < 0 or y < 0 or x == size or y == size:
        return 0
    new = list(map(list,puz))
    new[og_x][og_y] = puz[x][y]
    new[x][y] = 0
    return tuple(map(tuple,new))

def doit(start):
    global final_puzzle
    global size
    final_puzzle = ' '.join(map(str,flatten(final_puzzle)))
    # hold = str(start)
    start = flatten(start)
    # print(start)

    start = ' '.join(map(str,start))
    # for n in new_neigh(start):
        # print(n)
    # print(new_neigh)
    # sys.exit(1)
    que = []
    heap.heapify(que)
    closedSet = set()
    openSet = {}
    cameFrom = {}
    openSet[start] = [h_cost(start),0]
    hold = openSet[start]
    hold.append(start)
    heap.heappush(que, hold )
    # print(que)
    # sys.exit()
    i = 0
    while openSet:
        i += 1
        current = (heap.heappop(que))
        curGs = current[1]
        # print(curGs)
        current = current[2]
        # print(current)
        # sys.exit(1)
        closedSet.add(current)
        del openSet[current]
        
        if current == final_puzzle:
            print("solved in %d iterations" % i)
            path = get_path(cameFrom, current)
            print("steps to solve: %d" % len(path))
            return(path)

        for neigh in new_neigh(current):
            if neigh in closedSet:
                continue
            tmp_gscore = curGs + 1 
            if neigh not in openSet:
                openSet[neigh] = [ h_cost(neigh) + tmp_gscore, tmp_gscore]
                tmp = openSet[neigh]
                tmp.append(neigh)
                # print(tmp)
                # sys.exit(1)
                heap.heappush(que,tmp )
            elif tmp_gscore >= openSet[neigh][1]:
                continue
            cameFrom[neigh] = current
    print("not found")

def main():
    start = parsing(opening())
    init(start)
    doit(start)


main()
