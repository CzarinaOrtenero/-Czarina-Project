#EXERCISE 1 ARRAYS FUNCTIONS
#CZARINA J. ORTENERO

cars = ["audi","nissan","jaguar","hyundai","chevrolet", "porsche", "mercedez","honda"]
print cars
print "FASTEST:"
print cars[5]
num_cars = len(cars)
print(num_cars)
cars.append("acura")
print cars
cars.remove("audi")
print cars
cars.pop(4)
print cars
cars = ["audi"]
cars = cars * 10
print(cars)
