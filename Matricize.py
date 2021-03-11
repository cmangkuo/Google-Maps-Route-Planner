from getcoordinates import getcoordinates
from getCost import getCost
import googlemaps
import numpy as np


def Matricize(AddressBook, API_KEY):

	address = []
	cost_time =[[]]
	cost_distance = [[]]
	list_time = []
	list_distance = []

	for origin in AddressBook:
		address.append(origin)
		(lat, lng) = getcoordinates(origin)
		originC = str(lat) + ', ' + str(lng)
		for destination in AddressBook:
			(lat, lng) = getcoordinates(destination)
			destinationC = str(lat) + ', ' + str(lng)
			(dist, time) = getCost(originC, destinationC, API_KEY)
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
	AddressBook = open('Address Book.txt').readlines()
	file = open('API_KEY.txt').readlines()
	API_KEY = file[0]
	gmaps = googlemaps.Client(key = API_KEY)
	time, dist = Matricize(AddressBook, API_KEY)
	
	print(time)
	
	print('==============================')
	
	print(dist)