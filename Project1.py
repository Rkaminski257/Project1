my_str = """
    Date:           Country:                    New cases:
    9/1/2020        United States of America    37068
    9/2/2020        United States of America    31808
    9/3/2020        United States of America    42662
    9/4/2020        United States of America    39402
    9/1/2020        United Kingdom              1406
    9/2/2020        United Kingdom              1295
    9/3/2020        United Kingdom              1508
    9/4/2020        United Kingdom              1735
    9/1/2020        Japan                       527
    9/2/2020        Japan                       609
    9/3/2020        Japan                       598
    9/4/2020        Japan                       669
    9/1/2020        Mexico                      4129
    9/2/2020        Mexico                      3719
    9/3/2020        Mexico                      6476
    9/4/2020        Mexico                      4921
"""
my_list = [
    ("9/1/2020", "United States of America", 37068),
    ("9/2/2020", "United States of America", 31808),
    ("9/3/2020", "United States of America", 42662),
    ("9/4/2020", "United States of America", 39402),
    ("9/1/2020", "United Kingdom", 1406),
    ("9/2/2020", "United Kingdom", 1295),
    ("9/3/2020", "United Kingdom", 1508),
    ("9/4/2020", "United Kingdom", 1735),
    ("9/1/2020", "Japan", 527),
    ("9/2/2020", "Japan", 609),
    ("9/3/2020", "Japan", 598),
    ("9/4/2020", "Japan", 669),
    ("9/1/2020", "Mexico", 4129),
    ("9/2/2020", "Mexico", 3719),
    ("9/3/2020", "Mexico", 6476),
    ("9/4/2020", "Mexico", 4921),
]

class NewCases:
    def __init__(self, date, name, cases):
        self.date = date
        self.name = name
        self.cases = cases

    def print(self):
        print("Date: " + self.date + "\nCountry: "
                  + self.name + "\nNew cases: "
                  + str(self.cases))
