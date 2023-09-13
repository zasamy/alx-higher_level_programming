#!/usr/bin/python3
"""my list task"""


class MyList(list):
    """inherit from list"""

    def print_sorted(self):
        """print sorted list"""

        print(sorted(self))
