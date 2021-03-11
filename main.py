from getcoordinates import getcoordinates
from Matricize import Matricize
from minCost import minCost
import googlemaps


def main():
	AddressBook = open('Address Book.txt').readlines()
	file = open('API_KEY.txt').readlines()
	API_KEY = file[0]
	gmaps = googlemaps.Client(key = API_KEY)
	time_matrix, distance_matrix = Matricize(AddressBook, API_KEY)
	
	
	
	pathT, mintime= minCost(time_matrix)
	pathD, mindist = minCost(distance_matrix)
	print('=================================')
	print("Optimal Path (Time) \n =================================")
	print(pathT)
	mintime = mintime/60
	print(f'{mintime:.2f}' + " minutes")
	
	print('================================')
	print("Optimal Path (Distance) \n =================================")
	print(pathD)
	mindist = mindist/1000
	print(f'{mindist:.2f}' + " km")
	
if __name__ == "__main__":
	main()