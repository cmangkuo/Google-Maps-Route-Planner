import googlemaps

file = open('API_KEY.txt').readlines()
API_KEY = file[0]


gmaps = googlemaps.Client(key = API_KEY)

def getcoordinates(street, city, state):
    Location = street + ', ' + city + ', ' + state
    geocode = gmaps.geocode(Location)
    values = list(geocode[0].values())
    string = list(values[2].values()) 
    coordinates = string[1]
    
    latitude = coordinates['lat']
    longitude = coordinates['lng']
    return (latitude,longitude)
	
if __name__ == "__main__":	
	street = input("Enter street with number: ")
	city = input("Enter city: ")
	state = input("Enter state: ")


	(lat,lng) = getcoordinates(street,city,state)

	print(lat,lng)