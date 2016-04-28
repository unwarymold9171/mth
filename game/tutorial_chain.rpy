# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
#define e = Character('Eileen', color="#c8ffc8")

# The game starts here.
label tutorial_chain:

    s "You've created a new Ren'Py game."
    #stuff
    s "Once you add a story, pictures, and music, you can release it to the world!"
    
    if  mp.option == "Student" and mp.route == 1:
        $ mp.route = 2
        $ mp.save()
        jump tutorial_quotient
    elif mp.option == "Student":
        jump start
    return
