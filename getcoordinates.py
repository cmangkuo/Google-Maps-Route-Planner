import googlemaps

file = open('API_KEY.txt').readlines()
API_KEY = file[0]


gmaps = googlemaps.Client(key = API_KEY)

def getcoordinates(address):
	geocode = gmaps.geocode(address)
	values = list(geocode[0].values())
	string = list(values[2].values()) 
	for value in string:
		if (('lat' in value) and ('lng' in value)):
			coordinates = value
			break
	latitude = coordinates['lat']
	longitude = coordinates['lng']
	return (latitude,longitude)
	

if __name__ == "__main__":	
	address = input("Enter full address: ")
	(lat,lng) = getcoordinates(address)
	print(lat,lng)