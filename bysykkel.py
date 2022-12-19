import requests
from typing import Tuple, Dict
from math import sqrt



def available_docks() -> Dict[str, int]:
    station_response = requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json", headers={"Client-Identifier": "student-reiseplanleggingsprosjekt"}).json()['data']['stations']
    dict = {}
    for station in station_response:
        if station['num_docks_available'] > 0:
            dict[station['station_id']] = station['num_docks_available']
    return dict


def available_bikes() -> Dict[str, int]:
    station_response = requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json", headers={"Client-Identifier": "student-reiseplanleggingsprosjekt"}).json()['data']['stations']
    dict = {}
    for station in station_response:
        if station['num_bikes_available'] > 0:
            dict[station['station_id']] = station['num_bikes_available']
    return dict
    


def nearest_station(position: Tuple[int, int], type: int, lang: str) -> str:
    # type 0 indicates that you are looking for a bike
    # type 1 indicates that you are on a bike looking for a dock

    possible_stations = available_bikes() if type == 0 else available_docks()

    system_response = requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json", headers={"Client-Identifier": "student-reiseplanleggingsprosjekt"}).json()['data']['stations']
    min_distance = 100000000
    nearest_station = ''
    available_units = 0
    for station in system_response:
        if station['station_id'] not in possible_stations.keys():
            continue
        lat_diff = position[0]-station['lat']
        long_diff = position[1]-station['lon']
        distance = sqrt(lat_diff**2+long_diff**2)
        if distance <= min_distance:
            min_distance = distance
            nearest_station = station['name']
            available_units = possible_stations[station['station_id']]
    if lang == "en":
        return_sentence =  'The nearest station is ' + nearest_station + ' and there is ' + str(available_units)
        return_sentence += ' bikes.' if type == 0 else ' docks.'
    else:
        return_sentence =  'Den nærmeste stasjonen er ' + nearest_station + ' og det er ' + str(available_units)
        return_sentence += ' ledige sykler.' if type == 0 else ' ledige dokker.'
    return return_sentence



