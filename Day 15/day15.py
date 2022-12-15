from os.path import dirname, join
from z3 import Solver, Int, Abs

def main(part):
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    distance = []
    sensors = []
    beacons = set()
    for line in lines:
        line_arr = line.strip().split()
        sensor_x = int(line_arr[2][2:-1])
        sensor_y = int(line_arr[3][2:-1])
        beacon_x = int(line_arr[8][2:-1])
        beacon_y = int(line_arr[-1][2:])
        current_dist = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
        distance.append(current_dist)
        sensors.append((sensor_x, sensor_y))
        beacons.add((beacon_x, beacon_y))

    if part == 1:
        not_beacons = set()
        for i in range(len(distance)):
            not_beacons = fill_lines(sensors, distance, not_beacons, i, 1)
            not_beacons = fill_lines(sensors, distance, not_beacons, i, -1)
        print(len(not_beacons-beacons))
    else:
        solver = Solver()
        x = Int("x")
        y = Int("y")
        solver.add(0 <= x)
        solver.add(x <= 4000000)
        solver.add(0 <= y)
        solver.add(y <= 4000000)
        for i in range(len(distance)):
            sensor_x = sensors[i][0]
            sensor_y = sensors[i][1]
            solver.add(Abs(sensor_x-x) + Abs(sensor_y-y) > distance[i])
        solver.check()
        model = solver.model()
        print(model[x].as_long() * 4000000 + model[y].as_long())

def fill_lines(sensors, distance, not_beacons, i, shift):
    dist = abs(sensors[i][1] - 2000000)
    sensor_x = sensors[i][0]
    while dist <= distance[i]:
        not_beacons.add((sensor_x, 2000000))
        sensor_x += shift
        dist += 1
    return not_beacons

if __name__ == '__main__':
    main(1)
    main(2)