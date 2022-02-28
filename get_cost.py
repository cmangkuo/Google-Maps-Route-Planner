import requests


def get_cost(origin, destination, API_KEY):
    url = (
        "https://maps.googleapis.com/maps/api/distancematrix/json?origins="
        + origin
        + "&destinations="
        + destination
        + "&mode=driving&key="
        + API_KEY
    )
    response = requests.request("GET", url)
    output = "".join(response.text).split(",")

    cost = []
    for word in output:
        time = 0
        if "value" in word:
            time = word
            time = [int(s) for s in time.split() if s.isdigit()]
            cost.append(time[0])

    return cost


if __name__ == "__main__":
    from get_coordinates import get_coordinates
    from operator import add

    file = open("API_KEY.txt").readlines()
    API_KEY = file[0]

    addresses = open("Address Book.txt").readlines()
    address_list = []
    for address in addresses:
        address_list.append(address)
    total_cost = [0, 0]

    for x in range(len(address_list)):
        if x == len(address_list) - 1:
            y = 0
        else:
            y = x + 1
        origin = address_list[x]
        destination = address_list[y]
        cost = get_cost(origin, destination, API_KEY)
        total_cost = list(map(add, cost, total_cost))
    print("Original Time Cost (Min): " + str(total_cost[1] / 60))
    print("Original Distance Cost (km): " + str(total_cost[0] / 1000))
