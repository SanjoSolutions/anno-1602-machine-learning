def choose_island(islands, ships, number_of_players):
    islands = list(islands)
    number_of_islands = len(islands)
    if number_of_islands == 0:
        return None
    elif number_of_islands == 1:
        return islands[0]
    else:
        islands.sort(key=evaluate_island_suitability, reverse=True)
        return islands[0]


def evaluate_island_suitability(island):
    return calculate_island_size(island)


def calculate_island_size(island):
    return island.width * island.height
