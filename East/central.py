"""
Michael Patel
November 2019

"""


# Milwaukee
class Milwaukee:
    def __init__(self):
        self.roster = [
            "Giannis Antetokounmpo",
            "Khris Middleton",
            "Brook Lopez",
            "Eric Bledsoe",
            "Kyle Korver"
        ]

    # print team roster
    def print_roster(self):
        for player in self.roster:
            print(f'{player}')