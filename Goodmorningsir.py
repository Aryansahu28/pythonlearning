import time
timehour = int(time.strftime("%H"))
timemin = time.strftime("%M")
timesecs = time.strftime("%S")

if(timehour>5 and timehour < 12):
    print("Good Morning Sir ")

elif(timehour>00 and timehour<=16):
    print("Good Afternoon Sir")

else:
    print("Good Night")