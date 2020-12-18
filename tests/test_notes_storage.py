import unittest
from unittest.mock import mock_open, patch, MagicMock
from unittest import mock
from src.sample.NotesStorage import NotesStorage

class TestNotesStorage(unittest.TestCase):
    def setUp(self):
        self.temp = NotesStorage()

    def test_notes_storage_add(self):
        self.temp.add = MagicMock(return_value="Note added")
        self.assertEqual(self.temp.add(5), "Note added")

    def test_notes_storage_add_fail(self):
        self.temp.add = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.add, "ocenka")

    def test_notes_storage_clear(self):
        self.temp.clear = MagicMock(return_value=[])
        self.assertEqual(self.temp.clear(), [])

    def test_notes_storage_get_all(self):
        self.temp.getAllNotesOf = MagicMock(return_value=[5, 4, 3, 5])
        self.assertEqual(self.temp.getAllNotesOf("Krzysiu"), [5, 4, 3, 5])

    def test_notes_storage_get_all_failure(self):
        self.temp.getAllNotesOf = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.getAllNotesOf, 222)

if __name__ == "__main__":
    unittest.main()