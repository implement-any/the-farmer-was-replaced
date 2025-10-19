 # 각 드론의 동작이 완료되었는지 확인하는 함수
def wait_for_drones(drones):
	for i in range(len(drones)):
		wait_for(drones[i])