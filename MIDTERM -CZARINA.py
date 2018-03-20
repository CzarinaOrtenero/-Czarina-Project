# MIDTERM EXAMINATION
#CZARINA ORTENERO

def match_a():
    print ("Function match_a() \n")

    yna1 = input("Enter 1st input:")
    yna2 = input("Enter 2nd input:")
    yna3 = input("Enter 3rd input:")

    yna22 = []
    yna33 = []
    yna11 = []

    for i in yna1:
        if len(i) != 1:  # exclude character
            if i == i[::-1]:  # Palindrome checker
                yna11.append(i)

    for i in yna2:
        if len(i) != 1:  # exclude character
            if i == i[::-1]:  # Palindrome checker
                yna22.append(i)

    for i in yna3:
        if len(i) != 1:  # exclude character
            if i == i[::-1]:  # Palindrome checker
                yna33.append(i)

    print "1st output: ", len(yna11)
    print "2nd output: ", len(yna22)
    print "3rd output: ", len(yna33)


match_a()
print ("\n\n")


def front_x():
    print ("Function front_x()\n")

    yna1 = input("Enter 1st input:")
    yna2 = input("Enter 2nd input:")
    yna3 = input("Enter 3rd input:")

    yna11 = []
    yna111 = []
    yna22 = []
    yna222 = []
    yna33 = []
    yna333 = []

    for i in yna1:
        if i.startswith('x'):  # new list of strings that starts with 'x' from others
            yna11.append(i)
        else:
            yna111.append(i)  # new list of other strings

    print "1st output: ", sorted(yna11) + sorted(yna111)  # to alphabetically arranged

    for i in yna2:
        if i.startswith('x'):  # new list of strings that starts with 'x' from others
            yna22.append(i)
        else:
            yna222.append(i)  # new list of other strings

    print "2nd output: ", sorted(yna22) + sorted(yna222)  # to alphabetically arranged

    for i in yna3:
        if i.startswith('x'):  # new list of strings that starts with 'x' from others
            yna33.append(i)
        else:
            yna333.append(i)  # new list of other strings

    print "3rd output: ", sorted(yna33) + sorted(yna333)  # to alphabetically arranged


front_x()
