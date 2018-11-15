import sys
import heapq as heap
import settings

def make_goal():
    num_tile = settings.size * settings.size
    puzzle = [-1 for i in range(num_tile)]
    cur = 1
    x = 0
    ix = 1
    y = 0
    iy = 0
    while True:
        puzzle[x + y * settings.size] = cur
        if cur == 0:
            break
        cur += 1
        if x + ix == settings.size or x + ix < 0 or (ix != 0 and puzzle[x + ix + y*settings.size] != -1):
            iy = ix
            ix = 0
        elif y + iy == settings.size or y + iy < 0 or (iy != 0 and puzzle[x + (y+iy)*settings.size] != -1):
            ix = -iy
            iy = 0
        x += ix
        y += iy
        if cur == settings.size * settings.size:
            cur = 0

    return puzzle

def swapWithNb(puz, og_x, og_y, x, y, nb):
    if x < 0 or y < 0 or x == settings.size or y == settings.size:
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
    dic = {}
    for num in range(settings.size * settings.size):
        dic[num] = index_2d(num, settings.final_puzzle)
    return(dic)

def h_cost(puzzle):
    if settings.heristicChoice == 'md':
        return (manhat(puzzle))
    elif settings.heristicChoice == 'np':
        return (misplaced(puzzle))
    elif settings.heristicChoice == 'gt':
        return g_thing(puzzle, 0, 0)
    elif settings.heristicChoice == 'lc':
        return (manhat(puzzle) + lineByline(puzzle))
    elif settings.heristicChoice == 'gr':
        return (manhat(puzzle) * 5)
    elif settings.heristicChoice == 'uc':
        return (0)
    else:
        print("invalid heursitic")
        sys.exit(1)    

def manhat(puzzle):
    score = 0
    for x in range(settings.size):
        for y in range (settings.size):
            real_idx = settings.idx_dic[puzzle[x][y]]
            score += abs(x - real_idx[0]) + abs(y - real_idx[1])
    return(score)

def swap(puz, og_x, og_y, x, y):
    if x < 0 or y < 0 or x == settings.size or y == settings.size:
        return 0
    new = list(map(list,puz))
    new[og_x][og_y] = puz[x][y]
    new[x][y] = 0
    return tuple(map(tuple,new))

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
    count = 0
    for x in range(settings.size):
        for y in range(settings.size):
            if puzzle[x][y] == settings.final_puzzle[x][y]:
                count += 1
    return (settings.size * settings.size - count)

def g_thing(puzzle, nb, count):

    if (puzzle == settings.final_puzzle):
        return (count)
    while(index_2d(nb, puzzle) != index_2d(nb, settings.final_puzzle)):
        x,y = index_2d(nb, puzzle)
        num = settings.final_puzzle[x][y]
        currentX, currentY = index_2d(num, puzzle)
        puzzle = swapWithNb(puzzle, x, y, currentX, currentY, nb)
        count += 1
    return g_thing(puzzle, nb + 1, count)

def lineByline(puzzle):
    count = 0
    for x in range(len(puzzle)):
        count += check_line2(puzzle[x],'h', x)
        send = [t[x] for t in puzzle]
        count += check_line2(send,'v', x)
    return(count)

def check_line2(line, direction, idx):
    count = 0
    for i in range(len(line) - 1):
        for j in range(len(line) - i - 1):
            j += i + 1
            tmp = line[i]
            tmp2 = line[j]
            if line[i] == 0 or line[j] == 0:
                continue
            if direction == 'v':
                if settings.idx_dic[line[i]][1] == settings.idx_dic[line[j]][1] and idx == settings.idx_dic[line[i]][1]:
                    if  settings.idx_dic[line[i]][0] > settings.idx_dic[line[j]][0]:
                        count += 1
            else:
                if settings.idx_dic[line[i]][0] == settings.idx_dic[line[j]][0] and idx == settings.idx_dic[line[i]][0]:
                    if  settings.idx_dic[line[i]][1] > settings.idx_dic[line[j]][1]:
                        count += 1
    return count * 2

def opening():
    start = []
    # check correct number of arguments (just one for one file)

    if len(sys.argv) != 3:
        print("problem with args")
        print("usage: main.py [puzzle file] [md = Manhattan, lc = Linear conflict, gr = Greedy, np = not in place, gt = n-MaxSwap, uc = uniform cost]")
        sys.exit(1)
    else:
        settings.heristicChoice = sys.argv[2]
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
    settings.size = start.pop(0)
    settings.size = settings.size[0]

    #check puzzle y size
    if settings.size != len(start):
        print("error puzzle not correct size")
        sys.exit(1)

    # check puzzle x size
    for line in start:
        if len(line) != settings.size:
            print("error puzzle not correct size")
            sys.exit(1)

    # make list with correct numbers, remove numbers in actual, if anything left over crash
    correct =  list(range(settings.size * settings.size))
    try:
        check = [correct.remove(n) for line in start for n in line]
    except Exception:
        print("error : not sequentail numbers for size %d" % settings.size)
        sys.exit(1)
    if (len(correct) != 0):
        print("error : not sequentail numbers for size %d" % settings.size)
        sys.exit(1)
    return(tuple(tuple(line) for line in start))

def flatten(puz):
    a = list(x for y in puz for x in y)
    return(a)

def is_solvable(puz):

    inv = 0
    startidx = [puz.index(line) for line in puz for num in line if num == 0]
    finalidx = [settings.final_puzzle.index(line) for line in settings.final_puzzle for num in line if num == 0]
    g = abs(startidx[0] - finalidx[0])
    g += 1
    a = flatten(puz)
    final = flatten(settings.final_puzzle)

    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            j += i + 1
            if a[i] == 0 or a[j] == 0:
                continue
            if final.index(a[i]) >= final.index(a[j]):
                inv += 1

    if settings.size % 2 != 0:
        if inv % 2 == 0:
            return 0
        else:
            return(1)
    else:
        if inv % 2 == 0:
            if g % 2 != 0:
                return 0
            else:
                return (1)
        else:
            if g % 2 == 0:
                return 0
            else:
                return (1)

def init(start):
    realfin = []
    settings.final_puzzle = make_goal()
    for line in range(0, settings.size * settings.size, settings.size):
        realfin.append(settings.final_puzzle[line:line + settings.size])
    settings.final_puzzle = tuple(tuple(x) for x in realfin)
    settings.idx_dic = make_lookup_dic_heru()

def doit(start):
    if is_solvable(start) == 1:
        print("unsolvable")
        sys.exit(1)

    que = []
    heap.heapify(que)
    closedSet = set()
    openSet = {}
    cameFrom = {}
    openSet[start] = (h_cost(start),0)
    heap.heappush(que, openSet[start] + start )
    dups = {}
    i = 0
    j = 0
    most = 0
    while openSet:
        i += 1
        j -= 1
        if j > most:
            most = j
        current = (heap.heappop(que))
        curGs = current[1]
        current = current[2:]
        closedSet.add(current)
        del openSet[current]
        if current == settings.final_puzzle:
            print("solved in %d iterations" % i)
            path = get_path(cameFrom, current)
            print("steps to solve: %d" % len(path))
            print("time complexity: %d"% i)
            print("space complexity: %d"% (len(closedSet) + most))
            pathrev = reversed(path)
            for puz in pathrev:
                for inner in puz:
                    print(inner)
                print("\n",end='')
            return(path,i,most + len(closedSet))
        for neigh in find_neighbors(current):
            if neigh in closedSet:
                continue
            tmp_gscore = curGs + 1 
            if neigh not in openSet:
                openSet[neigh] = ( h_cost(neigh) + tmp_gscore, tmp_gscore)
                heap.heappush(que,(openSet[neigh][0], tmp_gscore) + neigh )
                j += 1
            elif tmp_gscore >= openSet[neigh][1]:
                continue
            cameFrom[neigh] = current
    print("There is no Solution for this Puzzle")







