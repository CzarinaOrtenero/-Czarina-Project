#CZARINA ORTENERO
#EXERCISE 5 "DICTIONARY"
print("REGIONS IN THE PHILIPPINES")
print ("1. Region I \n2. Region II \n3. Region III \n4. Region IV  \n5. Region V \n6. Region VI \n7. Region VII \n8. Region VIII \n9. Region IX \n10. Region X  \n11. Region XI \n12. Region XII  \n13. Region XIII \n14. NCR Region  \n15. CAR Region \n16. ARMM" )
def func():
    region = {"1":"ILOCOS REGION","2":"CAGAYAN VALLEY","3":"CENTRAL LUZON2","4":"A CALABARZON-B MIMAROPA","5":"BICOL REGION","6":"WESTERN VISAYAS","7":"CENTRAL VISAYAS","8":"EASTERN VISAYAS","9":"ZAMBOANGA PENINSULA","10":"NORTHERN MINDANAO","11":"DAVAO REGION","12":"SOCCSKSARGEN","13":"CARAGA REGION","14":"NATIONAL CAPITAL REGION","15":"CORDILLERA ADMINISTRAIVE REGION","16":"AUTONOMOUS REGION IN MUSLIM MINDANAO" }

    yna =input("\nREGION NO. ")

    if yna == 1:
        print region["1"]
    elif yna == 2:
        print region["2"]
    elif yna == 3:
        print region["3"]
    elif yna == 4:
        print region["4"]
    elif yna == 5:
        print region["5"]
    elif yna == 6:
        print region["6"]
    elif yna == 7:
        print region["7"]
    elif yna == 8:
        print region["8"]
    elif yna == 9:
        print region["9"]
    elif yna == 10:
        print region["10"]
    elif yna == 11:
        print region["11"]
    elif yna == 12:
        print region["12"]
    elif yna == 13:
        print region["13"]
    elif yna == 14:
        print region["14"]
    elif yna == 15:
        print region["15"]
    elif yna == 16:
        print region["16"]
    return func()
func()