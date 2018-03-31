#EXERCISE 8 QUEUES AND DEQUEUES
#CZARINA J. ORTENERO

import collections

d = collections.deque(xrange(10))
print "Normal queue", d

d.rotate(2)
print "\nRight rotation :", d

d1 = collections.deque(xrange(10))
d1.rotate(-5)
print "\nLeft rotation :", d1



