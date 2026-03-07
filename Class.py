class Fish:
    # Initialize a new Fish object.
    def __init__(self, year: int, population: int):
        self.year = year
        #self.name = name
        self.pop = population

    # Provide a developer-friendly string representation of the object.
    # output: string representation
    def __repr__(self):
        return "The Population at year {}, is {}".format(self.year, self.pop)

    def __eq__(self, other):
        return (self is other or
                type(other) == Fish and
                self.year == other.year and
               # self.name == other.name and
                self.pop == other.pop)

    # allows comparison of fish object
    def __lt__(self, other):
        return self.pop < other.pop