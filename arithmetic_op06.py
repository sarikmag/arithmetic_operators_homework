#Create a variable called 'number' with data type int.
number = 11
#Divide the number by 2 and assign number.
number = number / 2
#Find the fraction of the number and assing to a variable called 'answer'.
from math import floor
answer = number % (floor(number))
#Print the answer.
print(answer)
#Print the number.
print(number)