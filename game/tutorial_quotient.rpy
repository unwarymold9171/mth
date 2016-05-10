# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
#define e = Character('Eileen', color="#c8ffc8")

# The game starts here.
label tutorial_quotient:

    if  mp.option == "Teacher":
        s "So, you want me to teach the quotient rule."
    elif mp.route == 1:
        s "Okay I will first start by teaching you the quotient rule."
    else:
        s "So, you want to review the quotient rule."
    
    s "Okay, have you ever had a problem where you have to take the derivative of a function over another function?"
    
    s "You will end up having another fraction for the dervative, however, it will not be the same."
    
    s"A simple way to remember the quotient rule is this little ryhme. Low d high, less high d low, and don't forget to square below."
    
    # p "Yeah...I've had to do a few of those."
    # p ""
    
    if mp.route == 1:
        $ mp.route = 2
        $ mp.save()
    
    jump tutorial