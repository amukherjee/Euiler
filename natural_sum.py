print " This program will calculate the sum of all the multiples of 3 and 5 less than 10 "

sum_of_multiple = 0

for traverse in range(1000) :
  if (traverse % 3 == 0) or (traverse % 5 == 0) :
    multiple = traverse
    sum_of_multiple = sum_of_multiple + multiple
traverse = traverse + 1
#print "This entire list :", List
#Sum_of_list 
print "The Sum is =", sum_of_multiple

