from get_coordinates import get_coordinates
from get_cost import get_cost
import googlemaps
import numpy as np


def matricize(adress_book, API_KEY):

    address = []
    cost_time = [[]]
    cost_distance = [[]]
    list_time = []
    list_distance = []

    for origin in adress_book:
        address.append(origin)
        (lat, lng) = get_coordinates(origin)
        origin_coordinates = str(lat) + ", " + str(lng)
        for destination in adress_book:
            (lat, lng) = get_coordinates(destination)
            destination_coordinates = str(lat) + ", " + str(lng)
            (dist, time) = get_cost(
                origin_coordinates, destination_coordinates, API_KEY
            )
            list_time.append(str(time))
            list_distance.append(str(dist))
        cost_time.append(list_time)
        cost_distance.append(list_distance)
        list_time = []
        list_distance = []
    cost_time.pop(0)
    cost_distance.pop(0)

    distance_matrix = np.array(cost_distance)
    time_matrix = np.array(cost_time)

    return (time_matrix, distance_matrix)


if __name__ == "__main__":
    adress_book = open("Address Book.txt").readlines()
    file = open("API_KEY.txt").readlines()
    API_KEY = file[0]
    gmaps = googlemaps.Client(key=API_KEY)
    time, dist = matricize(adress_book, API_KEY)

    print(time)

    print("==============================")

    print(dist)
