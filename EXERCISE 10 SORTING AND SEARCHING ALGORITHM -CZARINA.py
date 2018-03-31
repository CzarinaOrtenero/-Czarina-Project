#EXERCISE 10 SORTING AND SEARCHING ALGORITHM
#CZARINA J. ORTENERO

def ynaSort(alist):
    sublistcount = len(alist)//3
    while sublistcount > 0:
      for start_position in range(sublistcount):
        gap_InsertionSort(alist, start_position, sublistcount)

      print("counting",sublistcount, "The name list is",nlist)

      sublistcount = sublistcount // 3

def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap

        nlist[position]=current_value


nlist = ["yna","aub","shiela","chow"]
ynaSort(nlist)
print(nlist)
