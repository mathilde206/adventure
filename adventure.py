from data import locations

directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

position = (0, 0)


def print_map(location):
    """
    :param location: one of the four possible locations
    :return: prints the map
    """
    north = ["H", "P"]
    south = ["L", "M"]

    if location == 'house':
        north[0] = "X"
    elif location == "lake":
        south[0] = "X"
    elif location == "park":
        north[1] = "X"
    else:
        south[1] = "X"

    print str(north) + "\n" + str(south)




def print_description(location):
    print locations[position]['description']




while True:
    location = locations[position]['name']
    print 'You are at the %s' % location
    print_description(location)
    print_map(location)

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_location:
            print 'to the %s is a %s' % (k, possible_location['name'])
            valid_directions[k] = possible_position

    direction = raw_input('which direction do you want to go?\n')
    position = valid_directions[direction]


