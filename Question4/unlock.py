"""
I got this question in an interview, I was nervous and had trouble thinking. This is my
implementation post interview. I did not use an LLM or coding assistant for this work
because this question is actually cool to have as an interviewee and I want to show
myself what I am capable of.

Scenario: You are an engineer for a lock company. You need to create a function that
unlocks the lock if the correct knock pattern has occurred.
The open method and knock listener method has already been created for you.
open_door() : opens the door attached to the lock
knock_listener(): returns a timestamp of when the knock occurred
"""

from typing import List

# My Notes:
# Formatting: put all this into a class and follow more OOP if expanding,
#             I am using seconds at a type int but could be type float,
# Security: What should be returned to the user if none of their attempts work?
# Future feats: implement open_door and knock_listener,


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

    user_timestamps = gather_user_tries(limit=limit, max_knocks=len(valid_pattern))

    user_tries = timestamps_to_intervals(user_timestamps)
    # conver user_tries to time intervals. each time interval being the
    # difference between the time stamps in user_tries

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
    user_timestamps = []

    if limit < 0:
        return user_timestamps

    listening = True

    while listening:
        knock_series = []
        while len(knock_series) <= max_knocks:
            time = knock_listener()
            knock_series.append(time)

        user_timestamps.append(knock_series)

        if len(user_timestamps) == limit:
            listening = False
    return user_timestamps


def timestamps_to_intervals(timestamps: List[int]) -> List[int]:
    """Returns a list of integers representing the duration between two timestamps.
    Assume the timestamps are is desc order: [oldest time, ... ,earliest time]
    """
    # what if the datastructure did not have ordered timestamps?

    intervals = []

    for i in range(len(timestamps) - 1):
        intervals.append(timestamps[i] - timestamps[i + 1])

    return intervals


def valid_knock(valid_pattern: List[int], user_tries: List[list]) -> bool:
    """Returns True if a subarray in user_tries matches valid_pattern.
    Args:
        valid_pattern: a list of ints representing valid time intervals in seconds
        user_tries: a list of ints representing valid time intervals in seconds
    """
    return True


if __name__ == "__main__":
    valid_pattern = [1, 2, 3]
    main(valid_pattern=valid_pattern, limit=3)
