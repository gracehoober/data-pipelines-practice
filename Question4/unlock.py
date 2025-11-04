"""
I got this question in an interview, I was nervous and had trouble thinking. This is my
implementation post interview. I did not use an LLM or coding assistant for this work.

Scenario: You are an engineer for a lock company. You need to create a function that
unlocks the lock if the correct knock pattern has occurred.
The open method and knock listener method has already been created for you.
open_door() : opens the door attached to the lock
knock_listener(): returns a timestamp of when the knock occurred
"""

import re
from typing import List


def open_door():
    """Opens the lock to open the door."""
    return True


def knock_listener():
    """Returns a timestamp of when a knock occurs in seconds."""
    return "timestamp"


def main(valid_pattern: List[int], limit: int = 1) -> None:
    """Handles the functionality to unlock a door.
    Args:
        valid_pattern: List of durations in seconds between knocks
    """

    user_tries = gather_user_tries(limit=limit, max_knocks=len(valid_pattern))

    if valid_knock(valid_pattern=valid_pattern, user_tries=user_tries):
        open_door()


def gather_user_tries(limit: int, max_knocks: int):
    """Returns an array of knocking attempts equal to the limit parameter.
    Each subarray contains timestamps of a knock limited by the len parameter.
        Example: user_tries = [[],[]]
    Args:
        limit: the number of attempts a user has to unlock the door.
        max_knocks: the max number of knocks in a single user attempt.
    """
    user_tries = []

    if limit < 0:
        return user_tries

    listening = True

    while listening:
        knock_series = []
        while len(knock_series) <= max_knocks:
            time = knock_listener()
            knock_series.append(time)

        user_tries.append(knock_series)

        if len(user_tries) == limit:
            listening = False
    return user_tries


def valid_knock(valid_pattern: List[int], user_tries: List[list]) -> bool:
    # TODO: implement
    return True


if __name__ == "__main__":
    valid_pattern = [1, 2, 3]
    main(valid_pattern=valid_pattern, limit=3)
