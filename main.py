from bysykkel import nearest_station
import sys

lat = float(sys.argv[0])
lon = float(sys.argv[1])
type = int(sys.argv[2])

position = (lat, lon)

near = nearest_station(position=position, type=type)
print(near)