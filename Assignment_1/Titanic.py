import csv


class Passenger(object):
    def __init__(self, id, surname, pclass, survived, sex):
        self.id = id
        self.surname = surname
        self.pclass = pclass
        self.survived = survived
        self.sex = sex

    def __repr__(self):
        return "(%d) %s, %s, %s, %s" % (
            self.id,
            self.surname,
            ["1st", "2nd", "3rd"][self.pclass - 1],
            ["Died", "Survived"][self.survived],
            ["Male", "Female"][self.sex]
        )

    def is_firstclass(self):
        return self.pclass == 1

    def survived(self):
        return self.survived


def make_passengers():
    idi = 0
    namei = 1
    pclassi = 2
    survivedi = 5
    sexcodei = 6
    passengers = []
    with open('./Titanic.csv', 'r') as csvfile:
        titanic_reader = csv.reader(csvfile)
        next(titanic_reader)
        for row in titanic_reader:
            id = int(row[idi])
            surname = row[namei].split(',')[0]
            if row[pclassi] == '*':
                continue
            pclass = {'1st': 1, '2nd': 2, '3rd': 3}[row[pclassi]]
            survived = int(row[survivedi])
            sex = int(row[sexcodei])
            passengers.append(Passenger(id, surname, pclass, survived, sex))
    return passengers


class Titanic(object):
    def __init__(self):
        self.passengers = make_passengers()

# Testing
# if __name__ == "__main__":
#     for p in make_passengers():
#         print(p)
