import requests



def getCost(origin, destination, API_KEY):
	url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + origin +"&destinations=" + destination +"&mode=driving&key=" +API_KEY
	response = requests.request("GET", url)
	output = ''.join(response.text).split(',')

	cost = []
	for word in output:
		time = 0
		if('value' in word):
			time = word
			time = [int(s) for s in time.split() if s.isdigit()]
			cost.append(time[0])

	return cost
	
	
	
if __name__ == "__main__":
	from getcoordinates import getcoordinates
	(lat, lng) = getcoordinates( '6762 Bernal Ave Ste 630, Pleasanton, CA' )
	origin = str(lat) + ', ' + str(lng)

	(lat, lng) = getcoordinates( '30065 Industrial Pkwy SW, Union City, CA' )
	destination = str(lat) + ', ' + str(lng)

	file = open('API_KEY.txt').readlines()
	API_KEY = file[0]
	
	print(getCost(origin,destination,API_KEY))
	print(getCost(destination,origin,API_KEY))