import sys

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
print(arr)
#remove size from start of arr and make it an int
size = arr.pop(0)
print(size)
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
print (correct)
try:
    check = [correct.remove(n) for line in arr for n in line]
except Exception:
    print("FATAL ERROR : not sequentail numbers for size %d" % size)
    sys.exit(1)
if (len(correct) != 0):
    print("FATAL ERROR : not sequentail numbers for size %d" % size)
    sys.exit(1)




    
    
    


















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