from cactus_util import cactus_sorting
from position_util import pos_move

def cactus():
	for x in range(get_world_size()):
		pos_move(x, 0)
		cactus_sorting(x, North)
	for y in range(get_world_size()):
		pos_move(0, y)
		cactus_sorting(y, East)
			
while True:
	cactus()
	harvest()