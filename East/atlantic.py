"""
Michael Patel
November 2019

"""


# Boston
class Boston:
    def __init__(self):
        self.roster = [
            "Kemba Walker",
            "Jayson Tatum",
            "Jaylen Brown",
            "Gordon Hayward",
            "Marcus Smart"
        ]

    # print team roster
    def print_roster(self):
        for player in self.roster:
            print(f'{player}')


# Brooklyn
class Brooklyn:
    def __init__(self):
        self.roster = [
            "Kyrie Irving",
            "Kevin Durant",
            "DeAndre Jordan",
            "Jarrett Allen",
            "Caris LeVert"
        ]

    # print team roster
    def print_roster(self):
        for player in self.roster:
            print(f'{player}')