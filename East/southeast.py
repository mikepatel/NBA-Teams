"""
Michael Patel
November 2019

"""


# Miami
class Miami:
    def __init__(self):
        self.roster = [
            "Jimmy Butler",
            "Tyler Herro",
            "Kendrick Nunn",
            "Goran Dragic",
            "Justise Winslow"
        ]

    # print team roster
    def print_roster(self):
        for player in self.roster:
            print(f'{player}')