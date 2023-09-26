#
# Try run this code before changing anything!
#
# Below is a choose your own adventure story
# You print out what's happening in the story
# Give users 3 options to choose from
# Print out something based on which option the user chooses
#
# Change the code below however you want! Feel free to add things too
#
print("You're walking in a forest and see a large bear. What do you do?")
print("1) Hide from the bear")
print("2) Fight the bear")
print("3) Run from the bear")
choice = input(": ")
choice = int(choice)
if choice == 1:
    print("You become one with the shadows. The bear frantically looks around.")
    print("The bear looks directly at you! You're sure the bear sees you.")
    print("But thankfully, it doesn't see you! The bear gives up its search and trots away.")
elif choice == 2:
    print("You try to fight the bear. This can't possibly go well... right?")
    print("How do you fight the bear?")
    print("1) Wrestle the bear")
    print("2) Punch the bear")
    print("3) Tickle the bear")
    choice = input(": ")
    choice = int(choice)
    if choice == 1 or choice == 2:
        print("You go up to the bear. As soon as you go up to it. It eats you.")
    else:
        print("You try to tickle the bear. It works wonders! The bear hates being tickled.")
        print("The bear quickly runs away!")
elif choice == 3:
    print("You run from the bear. It decides to chase you!")
    print("In no time, it catches up to you and knocks you down.")
    print("It then says something!")
    print("Bear: Sorry about that! I'm in a hurry to meet a friend.")
    print("The bear looks at its watch.")
    print("Bear: Holy cow! I'm quite late! Ta-ta!")
    print("The bear runs off.")
print("And that's the story of when you ran into a bear in a forest.")


#
# When you're done, you can try the first story, or keep messing with this story:
#   https://github.com/Fmccline/dlg-coding/blob/main/short_story.py
#