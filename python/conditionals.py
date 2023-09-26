#********************************
# Conditionals Coding Assignment
#********************************
#
#=======  INSTRUCTIONS ==========
# 
# 1) Copy and past this code into your coding space
#    - Click the button above to copy this code
#    - In your browser, press control and v (Ctrl+V) to paste
#
# 2) Go through each comment. The comments start with a #
#    Change the things that the comments say


#
# Problem 1) Name
#
name = input("Input your name: ")
# Change "Mr. Cline"
if name == "Mr. Cline":
    # Change the print statment to something else
    print("You're so cool and fun")
else:
    print("That's an ok name")


#
# Problem 2) Age
#
age = input("Input your age: ")
age = int(age)
# Change 26
if age == 26:
    # Change the print statment to something else
    print("That's a good age!")
else:
    print("That's an ok age")


#
# Problem 3) Bored
#
is_bored = input("Are you bored? ")
if is_bored == "Yes" or \
    is_bored == "YES" or \
    is_bored == "yes" or \
    is_bored == "y" or \
    is_bored == "yeah" or \
    is_bored == "ya":
    # Change the print statment to something else
    print("That's too bad!")
else:
    print("I'm glad you're not bored!")


#
# Problem 3) How you're doing
#
how_you_are = input("How are you? ")
if how_you_are == "bored":
    print("Bummer!")
elif how_you_are == "good":
    print("I'm glad you're doing good!")
# Add 1 or more elif statements
# Example:
# elif how_you_are == "bad":
#     print("That's too bad")
else:
    print("That's interesting that you feel " + how_you_are)


#
# When you're done:
#   - Raise your hand and tell me you're done
#   - If I'm busy, you can open a new tab (Ctrl+T). Keep your tab with this code on it open!
#   - In your new tab, go to online-python.com
#   - Then start on the short or long story
#
#