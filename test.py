import sys

arr = []
if (len(sys.argv) != 2):
    print("problem with number of args")
    sys.exit(1)
try:
    with open(sys.argv[1], 'r') as puzzle:
        arr = (puzzle.read().split("#"))
except Exception as e:
    print("problem reading file")
    print("Error info: %s" % e)
    sys.exit(1)

# # print (arr)
# # print(arr)
arr = [line.split() for line in arr if line[0] != '#']

print (arr)
for line in arr:
    for i in range(len(line) - 1):
        if line[i][0] == '#':
            del line[i:]
            break

print("after")
print(arr)
# sys.exit(1)               


try:
    arr = [list(map(int, lst)) for lst in arr]
except Exception:
    print("problem, puzzle contains non numbers")
    sys.exit(1)
size = arr.pop(0)
# print(size)
# print(arr)

if size != len(arr):
    print("error puzzle not correct size")
    sys.exit(1)

# print(arr[0][0])
# print(arr)