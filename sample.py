# keaton = (1,2)
# aylor = [3,4]
# phil = keaton + aylor
# print(phil)
from heapq import *

# keaton = {1:(1,2),2:(3,4),3:(5,6)}
# keaton[1] = (2,2)
# print(keaton)

keaton = [5,6,7,8]
heapify(keaton)
for i,j in enumerate(keaton):
    print(i,end =' ')
    print(j)
    if keaton[i] == 5:
       print ("did")

# heappop(keaton)

print(keaton)

