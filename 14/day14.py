import optparse

def move_robot(robot, space):
    x,y,dx,dy = robot
    return ( (x+dx) % space[0], (y+dy) % space[1], dx, dy )

def get_safety(robots, space):
    mid_x = space[0] // 2
    mid_y = space[1] // 2
    num_robots = [0,0,0,0]
    for robot in robots:
        if (robot[0] < mid_x) and (robot[1] < mid_y):
            num_robots[0] += 1
        elif (robot[0] < mid_x) and (mid_y < robot[1]):
            num_robots[1] += 1
        elif (mid_x < robot[0]) and (robot[1] < mid_y):
            num_robots[2] += 1
        elif (mid_x < robot[0]) and (mid_y < robot[1]):
            num_robots[3] += 1
    return num_robots[0]*num_robots[1]*num_robots[2]*num_robots[3]

def display_robots(robots,space):
    grid = [[' ' for col in range(space[0])] for row in range(space[1])]
    for robot in robots:
        robx,roby = robot[:2]
        grid[roby][robx] = 'x'
    return grid


if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)
    parser.add_option("-p", "--print", dest="print", help="print simulation steps", action="store_true", default=False)
    parser.add_option("-t", "--time", dest="time", help="simulation time", default=100, type=int)
    parser.add_option("-s", "--space", dest="space", help="simulation space", default='101,103', type=str)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        data = [line.strip().split() for line in f]

    robots = [tuple(int(i) for i in pos[2:].split(',')) + tuple(int(i) for i in vel[2:].split(',')) for pos, vel in data]
    #robots = [(2,4,2,-3)]
    space = tuple(int(i) for i in options.space.split(','))
    sim_step = options.time

    if options.dbg:
        print(robots)

    movement = {0 : robots}
    time = 0
    while time <= sim_step:
        time += 1
        movement[time] = [move_robot(robot,space) for robot in robots]
        robots = [move_robot(robot,space) for robot in robots]
        if options.print:
            print(f"TIME: {time}")
            [print(''.join(row)) for row in display_robots(robots,space)]

    
    part1 = get_safety(movement[100], space)
    print(f"Part1: {part1}")
