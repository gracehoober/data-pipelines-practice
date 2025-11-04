"""## Question 4:
I got this question in an interview, I was nervous and had trouble thinking. This is my
implementation post interview. I did not use an LLM or coding assistant for this work.

Scenario: You are an engineer for a lock company. You need to create a function that
unlocks the lock if the correct knock pattern has occurred.
The open method and knock listener method has already been created for you.
open_door() : opens the door attached to the lock
knock_listener(): returns a timestamp of when the knock occurred"""

from typing import List


def open_door():
    return True


def knock_listener():
    return "timestamp"


def main(valid_pattern: List[int]) -> None:
    """Handles the functionality to unlock a door.
    Args:
        valid_pattern: List of durations in seconds between knocks
    """

    # gather_user tries
    user_tries = []
    listening = True

    while listening:
        knock_series = []
        while len(knock_series) <= len(valid_pattern):
            time = knock_listener()
            knock_series.append(time)

        user_tries.append(knock_series)

        # limit user to three tries
        if len(user_tries) == 3:
            listening = False

    # Test user tries to determine validity


if __name__ == "__main__":
    valid_pattern = [1, 2, 3]
    main(valid_pattern=valid_pattern)
