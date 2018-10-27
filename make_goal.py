def make_goal(size):
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

print(make_goal(3))