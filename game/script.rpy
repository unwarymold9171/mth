# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define s = Character('Senpai', color="#c8ffc8")

#########################
# TODO: 
#       create routes
#       implement student vs teacher
#Fix atend of project:
#       remode the autoreset
#########################

init python:
    mp = MultiPersistent("MTH.TeachingMode")

# The game starts here.
label splashscreen:
    
    if mp.modeSelected == True:
        return
    else:
        $ s(_("What are you?"), interact=False)
        
        menu:
            "Teacher":
                $ mp.option = "Teacher"
                $ mp.modeSelected = True
                $ mp.route = 10
                $ mp.tutorials_first_time = True
                $ mp.save()
                return
                
            "Student":
                $ mp.option = "Student"
                $ mp.modeSelected = True
                $ mp.route = 0
                $ mp.tutorials_first_time = True
                $ mp.save()
                return
    
label start:
    
    $ tutorials_first_time = True
    
    s "Hi! My name is Senpai, and I'd like to welcome you to mth dervaderv tutorial."
    s "In this tutorial, we'll teach you how to do the Product Rule, Quotient Rule, and Chain Rule, so you can practice these dervadervs on your own."
    
    if mp.option == "Teacher" :
        jump tutorial
    else:
        jump tutorial_product
    
label tutorial:
    
    if mp.tutorials_first_time:
        $ s(_("What would you like to see?"), interact=False)
    else:
        $ s(_("Is there anything else you'd like to see?"), interact=False)
    
    $ mp.tutorials_first_time = False
    $ mp.save()
    
    if mp.route == 0:
        jump tutorial_product
    
    elif mp.route == 1:
        menu:
            "Product Rule":
                jump tutorial_product
            "Something New":
                jump tutorial_quotient
            "That's enough for now.":
                jump end
    elif mp.route == 2:
        menu:
            "Product Rule":
                jump tutorial_product
            "Quotient Rule":
                jump tutorial_quotient
            "Something New":
                jump tutorial_chain
            "That's enough for now.":
                jump end
    else:
        menu:
            "Product Rule":
                jump tutorial_product
            "Quotient Rule":
                jump tutorial_quotient
            "Chain Rule":
                jump tutorial_chain
            "That's enough for now.":
                jump end

label end:
    
    s "..."
    s "Thank you for viewing this tutorial."
    
    s "I will reset this for you."
    $ mp.modeSelected = False
    $ mp.save()
    
    window hide
    
    return
