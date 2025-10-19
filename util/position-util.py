def get_pos():
	return [get_pos_x(), get_pos_y()]

def get_dir(x = 0, y = 0):
	if x:
		unit_x = x / abs(x)
		return { 1: East, -1: West }[unit_x]
	if y:
		unit_y = y / abs(y)
		return { 1: North, -1: South }[unit_y]
		
def get_destination(axis, current_axis):
	return axis % get_world_size() - current_axis

def move_swap(x, y):
	des_x = get_destination(x, get_pos_x())
	des_y = get_destination(y, get_pos_y())
	
	if abs(des_x) > abs(des_y):
		for i in range(abs(des_x)):
			swap(West)
			move(West)
	else:
		for i in range(abs(des_y)):
			swap(South)
			move(South)
			
def pos_move(x, y):
	if x > get_world_size() - 1 or y > get_world_size() - 1:
		print("Maximum range exceeded, range: 0 ~", get_world_size())
		return
					
	des_x = get_destination(x, get_pos_x())
	des_y = get_destination(y, get_pos_y())
	
	dir_x = get_dir(des_x, 0)
	dir_y = get_dir(0, des_y)
		
	for i in range(abs(des_x)):
		move(dir_x)
		
	for i in range(abs(des_y)):
		move(dir_y)
	
def pos_reset():
	x = get_pos_x()
	y = get_pos_y()
		
	for i in range(x):
		move(West)
		
	for i in range(y):
		move(South)