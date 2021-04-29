class Computer:
    operatingSystem = "Windows 10"
    year = 2018
    screenSize = 13.3
    brand = "HP"

    def calcAge(self):
        print("The age of my computer is", 2021 - self.year, "years old.")


p1 = Computer()
p1.calcAge()
