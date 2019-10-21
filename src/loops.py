# while loop
c = 3
while c < 0 :
	print("a loop with c" , c)
	c -= 1

# for loop
# 0..4
for x in range(0,5):
	print("for loop with x " , x)

# for (i in range(begin,end, step))
for x in range(0,10,2):
	print("for loop inc 2 with x " , x)

for x in range(5,0,-1):
	print("for loop dec with x " , x)

# xrange(number): from 0 to number
for x in xrange(5):  #  0..4
	print("testing xrange: " , x)

name = 'Python'
for x in name:
	print("for loop with string: " , x)

# break and continue works in python as well
findTheX = 'sdfXsaf'
for x in findTheX:
	if x == "X":
		print("found the X, now exit")
		break

# with continue we finish current iteration and go for next
someVocals = '0a00i0e00u000a'
for x in someVocals:
	if x =='0':
		continue
	elif x =='a':
		print("a found")
	elif x=='e':
		print("e found")

# else clause ###### after for and while is executed after the normal
# execution of the iteration, but NOT when the execution has been
# interrupted by break, exceptions or returns.
counter = 0
for x in someVocals:
	if x == 'a':
		counter += 1
else:
	print("Total a letters found in " , someVocals , ": " , counter)
