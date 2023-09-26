### Instructions ###
#
# Copy and paste this code so that you can run it.
# After running the program, modify the code so that it keeps running until you guess right.
# Hint: You'll need to use a while loop to accomplish this.
#

import random

start_num = 0
end_num = 10
chosen_num = random.randint(start_num, end_num)
print("I picked a number between " + str(start_num) + " and " + str(end_num) + ".")
# have the user enter in a number (which is returned as a string)
guess = input("Guess which number I picked: ")
# turn guess into an integer using the int() function.
guess = int(guess)
if guess == chosen_num:
    print("Wow you guessed right!")
else:
    print("Sorry, that's not the number I picked. My number was " + str(chosen_num))
