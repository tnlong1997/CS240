import Titanic


def omega():
    # Write your code to generate omega here
    omega = Titanic.Titanic()
    print(len(omega.passengers))
    return omega.passengers


passengers = omega()


def survived(pasengers):
    # Write your code to generate the set of survivors here
    s = []
    for passenger in passengers:
        if passenger.survived:
            s = s + [passenger]
    print(len(s))
    return s


s = survived(passengers)


def first_class(passengers):
    # Write your code to generate the set of survivors here
    f = []
    for passenger in passengers:
        if passenger.is_firstclass():
            f = f + [passenger]
    print(len(f))
    return f


f = first_class(passengers)


def second_class(passengers):
    pass


def third_class(passengers):
    pass


def p_first_class_survivors(passengers):
    # Write your code to compute the probability
    # that a first class passenger survives here
    count = 0
    for passenger in passengers:
        if passenger.is_firstclass() and passenger.survived:
            count += 1
    print(count / len(passengers))
    return count / len(passengers)


p_first_class_survivors(passengers)


def p_survivor_given_first_class(passengers):
    # Write your code to compute the probability that a passenger survives,
    # given that they are travelling first class here
    count = 0
    for passenger in passengers:
        if passenger.survived:
            count += 1
    print(count / len(passengers))
    return count / len(passengers)


p_survivor_given_first_class(f)
