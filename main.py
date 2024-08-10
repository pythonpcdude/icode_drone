from easytello import tello

WAIT_TIME = 3
DISTANCE = 20
DEGREE = 30


def my_commands(drone: tello.Tello, cmd):
    global WAIT_TIME, DISTANCE, DEGREE

    if cmd == '0':
        drone.wait(WAIT_TIME)
    elif cmd == "1":
        drone.takeoff()
    elif cmd == "2":
        drone.land()
    elif cmd == "w":
        drone.forward(DISTANCE)
    elif cmd == "s":
        drone.back(DISTANCE)
    elif cmd == "a":
        drone.left(DISTANCE)
    elif cmd == "d":
        drone.right(DISTANCE)
    elif cmd == "q":
        drone.ccw(DEGREE)
    elif cmd == "r":
        drone.cw(DEGREE)
    elif cmd == "f":
        drone.up(DISTANCE)
    elif cmd == "g":
        drone.down(DISTANCE)
    elif cmd == "p":
        print("QUIT")
        
        
def validate(drone: tello.Tello, txt: str):
    commands = [
        "0", "1", "2", "w", "s", "a",
        "d", "q", "r", "f", "g", "p"
        ]
    if txt.lower() in commands:
        my_commands(drone, txt.lower())



def menu():
    global DISTANCE, DEGREE, WAIT_TIME
    print("make selection" +
          "\n0: wait ({})".format(WAIT_TIME) +
          "\n1: takeoff()" +
          "\n2: land ()" +
          "\nw: forward({})".format(DISTANCE) +
          "\ns: back({})".format(DISTANCE) +
          "\na: left({})".format(DISTANCE) +
          "\nd: right({})".format(DISTANCE) +
          "\nq: cww({})".format(DEGREE) +
          "\nr: cw({})".format(DEGREE) +
          "\nf: up({})".format(DISTANCE) +
          "\ng: down({})".format(DISTANCE) +
          "\np: quit({})"
          )


def run(drone: tello.Tello):
    response = None
    while response != "p":
        menu()
        response = input("\n> ")
        drone.wait(3)
        validate(drone, response)


if __name__ == '__main__':
    my_drone = tello.Tello()

    run(my_drone)
