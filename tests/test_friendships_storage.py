import unittest

from unittest.mock import mock_open, patch, MagicMock
from unittest import mock
from src.sample.FriendshipsStorage import FriendshipsStorage
from src.sample.Friendships import Friendships


class TestFriendshipsStorage(unittest.TestCase):

    def setUp(self):
        self.fs = Friendships()
        self.store = FriendshipsStorage()

    def test_friendships_storage_add(self):
        self.fs.make_friends("Grzes", "Wies")
        self.store.add = MagicMock(return_value="Added all friendships")
        self.store.add(self.fs)

        self.store.add.assert_called_once_with(self.fs)

    def test_friendships_storage_add_error(self):
        self.store.add = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.store.add, "lala")
        self.store.add.assert_called_once_with("lala")

    def test_friendships_storage_clear(self):
        self.store.clear = MagicMock(return_value=[])
        self.assertEqual(self.store.clear(), [])

    def test_friendships_storage_get_friends(self):
        self.store.get_all_friends = MagicMock(return_value=["Arek", "Marek"])
        self.assertEqual(self.store.get_all_friends("Jarek"), ["Arek", "Marek"])
        self.store.get_all_friends.assert_called_once_with("Jarek")

    def test_friendships_storage_get_friends_error(self):
        self.store.get_all_friends = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.store.get_all_friends, 11)


if __name__ == "__main__":
    unittest.main()