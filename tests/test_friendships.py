import unittest
from src.sample.Friendships import Friendships


class TestFriendships(unittest.TestCase):
    def setUp(self):
        self.temp = Friendships()

    def test_friendships_add_friend(self):
        self.temp.add_friend("Grzegorz", "Scooby")
        self.assertEqual(self.temp.dict, {"Grzegorz": ["Scooby"]})

    def test_friendships_add_friend_error(self):
        self.assertRaises(TypeError, self.temp.add_friend, "Grzegorz", 15)

    def test_friendships_make_friends(self):
        self.temp.make_friends("Jacek", "Jola")
        self.assertEqual(self.temp.dict, {"Jacek": ["Jola"], "Jola": ["Jacek"]})

    def test_friendships_make_friends_error(self):
        self.assertRaises(TypeError, self.temp.make_friends, 15, "Jolss")

    def test_friendships_get_friends_list(self):
        self.temp.add_friend("Young", "Thug")
        self.assertEqual(self.temp.get_friends_list("Young"), ["Thug"])

    def test_friendships_get_friends_list_error(self):
        self.assertRaises(TypeError, self.temp.get_friends_list, True)

    def test_friendships_are_friends(self):
        self.temp.make_friends("A", "B")
        self.assertEqual(self.temp.are_friends("A", "B"), True)

    def test_friendships_are_friends_error(self):
        self.assertRaises(TypeError, self.temp.are_friends, True, "Uuuu")


if __name__ == "__main__":
    unittest.main()