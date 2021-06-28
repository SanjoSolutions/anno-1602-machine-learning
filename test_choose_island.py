import unittest

from Island import Island
from choose_island import choose_island


class TestChooseIsland(unittest.TestCase):
    def test_choose_island(self):
        islands = {Island()}
        ships = set()
        number_of_players = 1
        island = choose_island(islands, ships, number_of_players)
        self.assertTrue(island in islands)

    def test_choose_bigger_island(self):
        island_0 = Island()
        island_0.width = 200
        island_0.height = 100

        island_1 = Island()
        island_1.width = 300
        island_1.height = 200

        islands = {island_0, island_1}
        ships = set()
        number_of_players = 1

        island = choose_island(islands, ships, number_of_players)

        self.assertEqual(island_1, island)


if __name__ == '__main__':
    unittest.main()
