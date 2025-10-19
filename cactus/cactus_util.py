from util import find
from plant_util import safe_plant
from position_util import move_swap, pos_move, pos_reset

def cactus_sorting(axis, dir):
	measures = list() # 선인장 크기를 저장하기 위한 List
	
	for y in range(get_world_size()):
		safe_plant(Entities.Cactus)
		measures.append(measure()) # measure() 함수로 검사한 선인장 크기 추가
		move(dir)
			
	for i in range(get_world_size()):
		minCactus = find(measures, min(measures)) # 제일 작은 선인장을 찾은 후 index 반환
		measures.pop(minCactus)
		if dir == North:
			pos_move(axis, minCactus + i)
			move_swap(axis, i)
		else:
			pos_move(minCactus + i, axis)
			move_swap(i, axis)