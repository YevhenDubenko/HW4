import random
from random import randint

y_num = input("Enter your choice of HomoSapiens: ")
r_num = randint(1, 10)
print("I am a robot, my choice is a number:", + r_num)
if int(y_num) == r_num:
    print("You're too smart for me man, you guessed it")
else:
    print("Try to replay me one more time")






