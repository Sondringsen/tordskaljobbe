from bysykkel import nearest_station
import sys

lat = sys.argv[1]
lon = sys.argv[2]
type = sys.argv[3]

position = (float(lat), float(lon))

near = nearest_station(position=position, type=type)
print(near)