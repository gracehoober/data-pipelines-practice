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

        self.assertEqual(result, [1, 2, 3])

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