import googlemaps
gmaps = googlemaps.Client(key = 'AIzaSyDSxFfdQSp-CnE9xHP_2N5H1FJ7apVSN58')

def getcoordinates(street, city, state):
    Location = street + ', ' + city + ', ' + state
    geocode = gmaps.geocode(Location)
    values = list(geocode[0].values())
    string = list(values[2].values()) 
    coordinates = string[1]
    
    latitude = coordinates['lat']
    longitude = coordinates['lng']
    return (latitude,longitude)
	
	
street = input("Enter street with number: ")
city = input("Enter city: ")
state = input("Enter state: ")


(lat,lng) = getcoordinates(street,city,state)

print(lat,lng)