from position_util import pos_move
from cactus_util import cactus_sorting
from drone_util import wait_for_drones

def horizontal_cactus():
	pos_move(get_pos_x(), 0)
	cactus_sorting(get_pos_x(), North)
		
def vertical_cactus():
	pos_move(0, get_pos_y())
	cactus_sorting(get_pos_y(), East)
	
def spawn_drones(drones_list, run, dir):
	for i in range(get_world_size()):
		if num_drones() < max_drones():
			drone = spawn_drone(run)
			drones_list.append(drone)
		else:
			run()
		move(dir)

while True:
	drones = list()
	spawn_drones(drones, horizontal_cactus, East)
	wait_for_drones(drones)
	spawn_drones(drones, vertical_cactus, North)
	wait_for_drones(drones)
	harvest()
	pos_move(0, 0)