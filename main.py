from bysykkel import nearest_station
import sys

lat = sys.argv[0]
lon = sys.argv[1]
type = sys.argv[2]

position = (lat, lon)
near = nearest_station(position=position, type=type)
print(near)