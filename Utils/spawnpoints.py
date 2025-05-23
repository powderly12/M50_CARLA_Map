import carla

  
client = carla.Client('localhost', 2000)
client.set_timeout(2.0)

# Get the world and spawn the ego vehicle
world = client.get_world()
blueprint_library = world.get_blueprint_library()

spawn_points = world.get_map().get_spawn_points()


for i, spawn_point in enumerate(spawn_points):
    world.debug.draw_string(spawn_point.location, str(i), life_time=1000)

# In synchronous mode, we need to run the simulation to fly the spectator ctrl+c to end script
while True:
    world.tick()
