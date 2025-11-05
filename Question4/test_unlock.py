import unittest
from unittest.mock import patch
from unlock import main


class TestUnlock(unittest.TestCase):
    @patch("unlock.open_door")
    @patch("unlock.knock_listener")
    def test_valid_knock_pattern_unlocks_door(
        self, mock_knock_listener, mock_open_door
    ):
        mock_knock_listener.side_effect = [10, 9, 7, 4]
        mock_open_door.return_value = True

        valid_pattern = [1, 2, 3]

        main(valid_pattern=valid_pattern, limit=1)
        mock_open_door.assert_called_once()

    @patch("unlock.open_door")
    @patch("unlock.knock_listener")
    def test_invalid_knock_pattern_does_not_unlock(
        self, mock_knock_listener, mock_open_door
    ):
        mock_knock_listener.side_effect = [10, 8, 5, 1]
        mock_open_door.return_value = True

        valid_pattern = [1, 2, 3]

        main(valid_pattern=valid_pattern, limit=1)
        mock_open_door.assert_not_called()


if __name__ == "__main__":
    unittest.main()
