# import random

GOAL_STATE = [1,2,3,4, 12,13,14,5 ,11,0,15,6,10,9,8,7]
lst = [9 ,13, 14, 11, 0 ,10, 15,  8, 12,  6,  7,  1, 5,  2,  3,  4]

sum_inversions = 0
for tile in [x for x in lst if x != 0]:
	before_tiles = GOAL_STATE[:GOAL_STATE.index(tile)]
	for after_tile in [x for x in lst[lst.index(tile):] if x != 0]:
		if before_tiles.count(after_tile):
			sum_inversions += 1
print(sum_inversions)


