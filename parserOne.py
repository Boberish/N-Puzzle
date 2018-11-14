import sys
import cProfile
import heapq as heap
import settings
# import numpy

#######globals:
# final_puzzle = []
# size = 0
# idx_dic = {}



# final_puzzle = ((1,2,3),(8,0,4),(7,6,5))
# final_puzzle = ((1,2,3,4),(12,13,14,5),(11,0,15,6), (10,9,8,7))

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

def swap(puz, og_x, og_y, x, y):
    if x < 0 or y < 0 or x == settings.size or y == settings.size:
        return 0
    np = numpy.array(puzz)
    print(np)
    sys.exit(0)
    new = list(list(line) for line in puz)
    # if og_x == x:

    new[og_x][og_y] = puz[x][y]
    new[x][y] = 0
    return tuple(tuple(line) for line in new)

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
    # global idx_dic
    # if (str(sys.argv[2]) == "mp"):
    #     return (misplaced(puzzle))
    # if (str(sys.argv[2]) == "gt"):
    #     ret = g_thing(puzzle, 0, 0)
    #     return (ret)
    score = 0

    for x in range(settings.size):
        for y in range (settings.size):
            real_idx = settings.idx_dic[puzzle[x][y]]
            score += abs(x - real_idx[0]) + abs(y - real_idx[1])
    # return(score)
    return((score * 5))
    # return(score + linear_conflicts(puzzle))

# def swap(puz, og_x, og_y, x, y):
#     if x < 0 or y < 0 or x == size or y == size:
#         return 0
#     new = list(list(line) for line in puz)
#     # np = numpy.array(puz)

#     # print(np)
#     # sys.exit(1)
#     # puz = puz
#     new[og_x][og_y] = puz[x][y]
#     new[x][y] = 0


#     return tuple(tuple(line) for line in new)

def swap(puz, og_x, og_y, x, y):
    if x < 0 or y < 0 or x == settings.size or y == settings.size:
        return 0
    new = list(map(list,puz))
    # np = numpy.array(puz)
    # new = [row.copy() for row in puz]
    # print(new)
    # sys.exit(1)
    # print(np)
    # sys.exit(1)
    # puz = puz
    new[og_x][og_y] = puz[x][y]
    new[x][y] = 0


    return tuple(map(tuple,new))


# def swap(puz, og_x, og_y, x, y):
#     if x < 0 or y < 0 or x == size or y == size:
#         return 0
#     # new = list(list(line) for line in puz)
#     np = numpy.array(puz)

#     # print(np)
#     # sys.exit(1)
#     # puz = puz
#     np[og_x][og_y] = puz[x][y]
#     np[x][y] = 0
#     print(tuple(map(tuple,np)))
#     sys.exit(1)
#     return tuple(map(tuple,np))

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
    # global idx_dic

    if (puzzle == settings.final_puzzle):
        return (count)
    while(index_2d(nb, puzzle) != index_2d(nb, settings.final_puzzle)):
        x,y = index_2d(nb, puzzle)
        num = settings.final_puzzle[x][y]
        currentX, currentY = index_2d(num, puzzle)
        puzzle = swapWithNb(puzzle, x, y, currentX, currentY, nb)
        count += 1
    return g_thing(puzzle, nb + 1, count)

def linear_conflicts(puzzle):
    # global idx_dic
    hold = 0
    hold2 = 0
    holddic = {}
    count = 0

    for x in range(settings.size):
        hold = 0
        for y in range (settings.size):
            Cx,Cy = x,y
            Rx, Ry = settings.idx_dic[puzzle[x][y]]
            if Cx == Rx and Cy != Ry:
                hold += 1
                if hold > 1:
                    count += check_line2(puzzle[Cx], 'h', 0)
                    break

    for y in range(settings.size):
        hold = 0
        for x in range (settings.size):
            Cx,Cy = x,y
            Rx, Ry = settings.idx_dic[puzzle[x][y]]
            # tmp = puzzle[Cx][Cy]
            if Cx != Rx and Cy == Ry:
                hold += 1
                if hold > 1:
                    send = [thing[Cy] for thing in puzzle]
                    count += check_line2(send, 'v', 0)
                    break
    return(count)

def lineByline(puzzle):
    count = 0
    for x in range(len(puzzle)):
        count += check_line2(puzzle[x],'h', x)
        send = [t[x] for t in puzzle]
        # send = send[::-1]
        count += check_line2(send,'v', x)
    # if count > 4:
    # print (puzzle)
    # sys.exit()
    return(count)

def check_line(puzzle):
    g_pos = {}
    # global idx_dic
    count = 0
    for i,num in enumerate(puzzle):
        g_pos[i] = settings.idx_dic[num]

    for i in range(len(puzzle) - 1):
        for y in range(len(puzzle) - 1):
            y = i
            if puzzle[i] == 0 or puzzle[y + 1] == 0:
                continue
            if g_pos[i][0] == g_pos[1 + y][0]:
                if g_pos[i][1] > g_pos[1 + y][1]:
                    # count += 1
                    return(2)
    # return(count * 2)


def check_line2(line, direction, idx):
    # global idx_dic
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
                if settings.idx_dic[line[i]][1] == settings.idx_dic[line[j]][1] and idx == settings.idx_dic[line[i]][1]:
                    if  settings.idx_dic[line[i]][0] > settings.idx_dic[line[j]][0]:
                        count += 1
            else:
                if settings.idx_dic[line[i]][0] == settings.idx_dic[line[j]][0] and idx == settings.idx_dic[line[i]][0]:
                    if  settings.idx_dic[line[i]][1] > settings.idx_dic[line[j]][1]:
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
        print("FATAL ERROR : not sequentail numbers for size %d" % settings.size)
        sys.exit(1)
    if (len(correct) != 0):
        print("FATAL ERROR : not sequentail numbers for size %d" % settings.size)
        sys.exit(1)
    return(tuple(tuple(line) for line in start))

def flatten(puz):
    a = list(x for y in puz for x in y)
    return(a)


def is_solvable(puz):
    # global idx_dic

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
            # tmp1 = a[i]
            # tmp2 = a[j]
            if final.index(a[i]) >= final.index(a[j]):
                inv += 1

    if settings.size % 2 != 0:
        if inv % 2 == 0:
            print("solvable")
            return 0
        else:
            print ("UNSOLVABLE")
            return(1)
            # sys.exit(1)
    else:
        if inv % 2 == 0:
            if g % 2 != 0:
                print("solvable")
                return 0
            else:
                print("UNSOLVABLE")

                return (1)
            # sys.exit(1)

        else:
            if g % 2 == 0:
                print("solvable")
                return 0
            else:
                print("unsolvable")
                return (1)
            # sys.exit(1)



def init(start):
    # global idx_dic
    # print("idx in init = ", settings.idx_dic)
    realfin = []
    # start = tuple(tuple(line) for line in start)
    settings.final_puzzle = make_goal()
    for line in range(0, settings.size * settings.size, settings.size):
        realfin.append(settings.final_puzzle[line:line + settings.size])
    settings.final_puzzle = tuple(tuple(x) for x in realfin)
    settings.idx_dic = make_lookup_dic_heru()


def slow(que, neigh):
    for i,j in enumerate(que):
        if j[2:] == neigh:
            del que[i]



def doit(start):
    # is_solvable(start)

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
        # if i == 100000:
        #     sys.exit(1)
        current = (heap.heappop(que))
        # try:
        #     while dups[current] == 0:
        #         del dups[current]
        #         current = (heap.heappop(que))
        # except:
        #     pass
        curGs = current[1]
        current = current[2:]

        closedSet.add(current)
        del openSet[current]

        if current == settings.final_puzzle:
            print("solved in %d iterations" % i)
            path = get_path(cameFrom, current)
            print("steps to solve: %d" % len(path))
            return(path)
            # for puz in path:
            #     for inner in puz:
            #         print(inner)
            #     print("\n",end='')
            # sys.exit(0)

        for neigh in find_neighbors(current):
            if neigh in closedSet:
                continue
            tmp_gscore = curGs + 1 # distance from current to neighbor is always 1 here
            if neigh not in openSet:
                openSet[neigh] = ( h_cost(neigh) + tmp_gscore, tmp_gscore)
                heap.heappush(que,(openSet[neigh][0], tmp_gscore) + neigh )

            elif tmp_gscore >= openSet[neigh][1]:
                continue
            # else:
            #     dups[openSet[neigh] + neigh] = 0
            #     openSet[neigh] = ( h_cost(neigh) + tmp_gscore, tmp_gscore)
            #     heap.heappush(que,(openSet[neigh][0], tmp_gscore) + neigh)

            cameFrom[neigh] = current
    print("not found")






# arr = (4,1,((1,2,3),(2,3,4)(2,3,4)))
