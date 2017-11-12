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


def print_current_location(position):
    """
    :param position: a tuple with the coordinates of where the player currently is -
    :return: prints information about where the user is
    """
    location = locations[position]['name']
    print 'You are at the %s' % location
    print locations[position]['description']
    print_map(location)


def get_valid_direction(position):
    """
    :param position: a tuple with the coordinates of where the player currently is
    :return: the list of directions that are attainable from where the player currently is
    """
    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_location:
            valid_directions[k] = possible_position
    return valid_directions



while True:
    print_current_location(position)
    get_valid_direction(position)

    for key in get_valid_direction(position):
        print 'to the %s is a %s' % (key, locations[get_valid_direction(position)[key]]['name'])

    direction = raw_input('which direction do you want to go?\n')

    while not get_valid_direction(position).get(direction):
        direction = raw_input('which direction do you want to go?\n')
    else:
        position = get_valid_direction(position)[direction]
