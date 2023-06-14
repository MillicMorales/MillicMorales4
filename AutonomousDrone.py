import time

class AutonomousDrone:
    def __init__(self):
        self.position = (0, 0, 0)
        self.velocity = (0, 0, 0)

    def takeoff(self):
        print("The drone is taking off...")
        time.sleep(2)
        self.velocity = (0, 0, 5)
        print("The drone is now airborne.")

    def fly_to(self, x, y, z):
        print("Flying to destination...")
        time.sleep(2)
        self.position = (x, y, z)
        print("Destination reached.")

    def land(self):
        print("Preparing for landing...")
        time.sleep(2)
        self.velocity = (0, 0, 0)
        print("The drone has landed.")

def main():
    drone = AutonomousDrone()

    # Take off
    drone.takeoff()

    # Fly to a destination
    drone.fly_to(10, 10, 5)

    # Land
    drone.land()

if __name__ == "__main__":
    main()
