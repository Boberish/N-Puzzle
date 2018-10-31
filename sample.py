# keaton = (1,2)
# aylor = [3,4]
# phil = keaton + aylor
# print(phil)
from heapq import *

# keaton = {1:(1,2),2:(3,4),3:(5,6)}
# keaton[1] = (2,2)
# print(keaton)

keaton = [1,2,3,4]
heapify(keaton)
for i in range(len(keaton) - 1):
    if keaton[i] == 3:
       del keaton[i]

# heappop(keaton)

print(keaton)

