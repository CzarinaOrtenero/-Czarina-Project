#CZARINA ORTENERO
#EXERCISE 4 "FUNCTION"
print("CPE SUBJECTS")
print ("1. MAJOR SUBJECTS \n2. MINOR SUBJECTS")
def func():
    subjects = {"MAJOR":"CIRCUITS \nSOFTWARE ENGINEERING \nDATA STRUCTURE \n","MINOR": "INTEGRAL CALCULUS \nCOLLEGE PHYSICS \nPHILIPPINE LITERATURE"}
    yna =input("\nsubject type: ")

    if yna == 1:
        print subjects["MAJOR"]
    elif yna == 2:
        print subjects["MINOR"]
    return func()
func()
