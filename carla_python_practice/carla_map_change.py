#!/usr/bin/env python3
import carla
import time, sys
TOWN = "Town15"

HOST, PORT = "127.0.0.1", 2000
def main():
    client = carla.Client(HOST, PORT)
    client.set_timeout(10.0)
    print(f"Loading {TOWN} ... ")
    client.load_world(TOWN)
    while True:
        try:
            if
            client.get_world().get_map().name.endswith(TOWN):
                break
        except RuntimeError:
            pass
        time.sleep(0.1)
    world = client.get_world()
    spawns = world.get_map().get_spawn_points()
    if spawns:
        sp = spawns[0]
        loc = sp.location; loc.z += 60.0
        rot = carla.Rotation(pitch=-90)
        world.get_spectator().set_transform(carla.Transform(loc, rot))
    print(f"Success to change {TOWN} ...")
    if __name__ == "__main__":
        main()