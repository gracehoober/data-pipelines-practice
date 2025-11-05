import unittest
from unittest import mock
from unittest.mock import patch
from unlock import gather_user_tries, main, valid_knock, timestamps_to_intervals


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

    @patch("unlock.open_door")
    @patch("unlock.knock_listener")
    def test_series_of_knocks_success(self, mock_knock_listener, mock_open_door):
        mock_knock_listener.side_effect = [10, 8, 5, 1]
        mock_open_door.return_value = True

        valid_pattern = [1, 2, 3]

        main(valid_pattern=valid_pattern, limit=1)
        mock_open_door.assert_not_called()

    @patch("unlock.open_door")
    @patch("unlock.knock_listener")
    def test_series_of_knocks_fails(self, mock_knock_listener, mock_open_door):
        pass


class TestGatherUserTries(unittest.TestCase):
    @patch("unlock.knock_listener")
    def test_limit_of_zero(self, mock_knock_listener):
        mock_knock_listener.side_effect = [1, 2, 3]

        result = gather_user_tries(limit=0, max_knocks=3)

        assert result == []

    @patch("unlock.knock_listener")
    def test_max_knocks_zero(self, mock_knock_listener):
        mock_knock_listener.side_effect = [4]

        result = gather_user_tries(limit=1, max_knocks=0)

        assert result == [[4]]

    @patch("unlock.knock_listener")
    def test_max_knocks_and_limit(self, mock_knock_listener):
        mock_knock_listener.side_effect = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        result = gather_user_tries(limit=3, max_knocks=2)

        assert result == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class TestValidKnock(unittest.TestCase):
    def test_valid_knock_returns_true_for_matching_pattern(self):
        valid_pattern = [1, 2, 3]
        user_tries = [[2, 3, 4], [1, 2, 3], [5, 6, 7]]

        result = valid_knock(valid_pattern, user_tries)

        self.assertTrue(result)

    def test_valid_knock_returns_false_for_no_match(self):
        valid_pattern = [1, 2, 3]
        user_tries = [[2, 3, 4], [5, 6, 7]]

        result = valid_knock(valid_pattern, user_tries)

        self.assertFalse(result)


class TestTimestampsToIntervals(unittest.TestCase):

    def test_converts_single_series_to_intervals(self):
        timestamp_series = [[10, 9, 7, 4]]
        result = timestamps_to_intervals(timestamp_series)

        self.assertEqual(result, [[1, 2, 3]])

    @patch("unlock.open_door")
    @patch("unlock.knock_listener")
    def test_multiple_attempts_unlocks_on_second_try(
        self, mock_knock_listener, mock_open_door
    ):
        mock_knock_listener.side_effect = [
            # First attempt (4 knocks for pattern of length 3)
            10,
            8,
            5,
            1,
            # Second attempt (4 knocks)
            20,
            19,
            17,
            14,
        ]
        mock_open_door.return_value = True

        valid_pattern = [1, 2, 3]
        main(valid_pattern=valid_pattern, limit=2)

        mock_open_door.assert_called_once()


if __name__ == "__main__":
    unittest.main()
