from datetime import datetime
import time
import random
# list of odd numbers
Odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
# method call to a variable called right_this_minute we use () to invote the method call today from datetime submodule which is part of the datetime module and we use minute atribute to get the minutes
# baically we invole a metheid to spit out time and tehn we just pick the minute and assign it to the variable right-this-miute
for i in range(5):
    # we look over 5 time and we use the sleep (i) whichis also 5 so sleep 5 seconds then do it agai and again
    Right_This_Minute = datetime.today().minute
    if Right_This_Minute in Odds:
        print("This minute seems a little odd.")
    else:
        print("not an odd minute.")
    #we create a variable wait_time that takes a random intever from 1 to 60
    wait_time = random.randint(1, 60)
    #we assing the random integer to time.sleep
    time.sleep(wait_time)
