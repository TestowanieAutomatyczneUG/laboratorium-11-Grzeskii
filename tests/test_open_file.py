import unittest
from unittest.mock import mock_open, patch, MagicMock
from unittest import mock
from src.sample.OpenFile import OpenFile


class TestOpenFile(unittest.TestCase):

    def setUp(self):
        self.temp = OpenFile()
    
    def test_open_file_read(self):
        open_test = mock_open(read_data="jakies cos tutaj jest")
        path = "file.txt"

        with patch('builtins.open', open_test):
            self.assertEqual("jakies cos tutaj jest\n", self.temp.read(path))

    def test_open_file_write(self):
        write_test = mock_open(read_data="to jest tekst")
        path = "file.txt"

        with patch("builtins.open", write_test):
            self.temp.write(path, "to jestt tez tekst")

        write_test.assert_called_once_with(path, "w+")

    @mock.patch('src.sample.OpenFile.os')
    def test_open_file_delete_success(self, mock_os):
        mock_os.path = MagicMock()
        mock_os.path.exists.return_value = True
        path = "file.txt"

        self.temp.delete(path)

        mock_os.remove.assert_called_with(path)

    @mock.patch('src.sample.OpenFile.os')
    def test_open_file_delete_failure(self, mock_os):
        mock_os.path = MagicMock()
        mock_os.path.exists.return_value = False
        path = "file.txt"

        self.assertRaises(Exception, self.temp.delete, path)


if __name__ == '__main__':
    unittest.main()
