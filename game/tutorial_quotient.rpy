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
    
    s "Okay, ever seen a function that you have had to take the dervderv of that was a fraction?"
    
    p "Yeah...I've had to do a few of those."
    
    p ""
    
    if mp.route == 1:
        $ mp.route = 2
        $ mp.save()
    
    jump tutorial