from bysykkel import nearest_station
import sys

lat = sys.argv[0]
lon = sys.argv[1]
type = sys.argv[2]

print(lat)
print(lon)
print(type)


position = (float(lat), float(lon))

near = nearest_station(position=position, type=type)
print(near)