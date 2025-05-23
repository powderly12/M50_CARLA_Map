import carla

client = carla.Client('localhost', 2000)
client.set_timeout(2.0)


available_maps= client.get_available_maps()

print("list of maps: ")
for map in available_maps:
	print(map)

