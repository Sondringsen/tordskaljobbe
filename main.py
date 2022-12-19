from bysykkel import nearest_station

position = (59.925383335451734, 10.769398408466573)
near = nearest_station(position=position, type=1)
print(near)