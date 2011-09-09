#convert_temp.py

print "Do you want to convert..."
print "(1) F to C"
print "(2) C to F"

conv = input ("Enter number for desired option ")


def tempc():
   temp = input("Enter teprature in C: ")
   temp = round ( (temp * ( 9.0 / 5.0 ) ) + 32 )
   print temp, "degrees F"

def tempf():
   temp = input("Enter temprature in F: ")
   temp = round ( (temp - 32) * ( 5.0 / 9.0 ), 1)
   print temp, "degrees C"

if conv == 1:
   tempf()

if conv == 2:
   tempc()

