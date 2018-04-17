#Czarina Ortenero


def duplicate():
    Czarina = input("Enter numbers here: ")
    Czarina = list(Czarina)
    yna = []
    ynaort = []

    for c in Czarina:
        Czarina.count(c)
        if Czarina.count(c) != 1:
                yna.append(c)
        elif Czarina.count(c) == 1:
                ynaort.append(c)

    set(ynaort)
    print ynaort
    return(duplicate())

duplicate()