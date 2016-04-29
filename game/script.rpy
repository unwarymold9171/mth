#########################
# TODO: 
#       create routes
#       implement student vs teacher
#       Fix atend of project:
#       remove the autoreset
#
#########################

init python:
    mp = MultiPersistent("MTH.TeachingMode")

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define textless = Character('', color="#000000")
define s = Character("[mp.sName]", color="#c8ffc8")
define player = Character("[mp.playerName]")

label reset:
    
    textless "Reseting modeSelected"
    $ mp.modeSelected = False
    $ mp.save()
    textless "Jumping to splashcrween"
    jump splashscreen
    
# The game starts here.
label splashscreen:
    
    if mp.modeSelected == True:
        return
    else:
        $ textless(_("What are you?"), interact=False)
        menu:
            "Teacher":
                $ mp.option = "Teacher"
                $ mp.modeSelected = True
                $ mp.route = 10
                $ mp.tutorials_first_time = True
                $ mp.sName = "Student"
                $ mp.save()
                return
                
            "Student":
                $ mp.option = "Student"
                $ mp.modeSelected = True
                $ mp.route = 0
                $ mp.tutorials_first_time = True
                $ mp.sName = "Senpai"
                $ mp.save()
                return
    
label start:
    
    $ tutorials_first_time = True
    
    if mp.route == 0 or mp.route == 10:
        if mp.route == 0:
            $ mp.playerName = renpy.input("What is your name?")
            $ mp.playerName = mp.playerName.strip()
            if not mp.playerName:
                $ mp.playerName = "Pat Smith"
            $ mp.save()
        else:
            $ mp.playerName = "Teacher"
            $ mp.save()
        
        
        s "Hi! My name is [mp.sName], and I'd like to welcome you to mth dervaderv tutorial."
        
        if mp.route == 0:
            s "What is your name?" 
            player "My name is [mp.playerName]."
        
        s "Okay, [mp.playerName]. In this tutorial, we'll teach the Product Rule, Quotient Rule, and Chain Rule, so you can practice these dervadervs on your own."
    else:
        s "Welcome back, [mp.playerName]. "
        if mp.route == 1:
            extend "I have so far taught you the Product Rule"
        elif mp.route == 2:
            extend "I have so far taught you the Product Rule and the Quotient Rule"
        elif mp.route == 3:
            extend "I have so far taught you all three of the rules"
    
    jump tutorial
    
label tutorial:
    
    if tutorials_first_time:
        $ s(_("What would you like to see?"), interact=False)
    else:
        $ s(_("Is there anything else you'd like to see?"), interact=False)
    
    $ tutorials_first_time = False
    
    if mp.route == 0:
        menu:
            "Something new":
                jump tutorial_product
            "That's enough for now.":
                jump end
    
    elif mp.route == 1:
        menu:
            "Product rule":
                jump tutorial_product
            "Something new":
                jump tutorial_quotient
            "That's enough for now.":
                jump end
    elif mp.route == 2:
        menu:
            "Product rule":
                jump tutorial_product
            "Quotient rule":
                jump tutorial_quotient
            "Something new":
                jump tutorial_chain
            "That's enough for now.":
                jump end
    else:
        menu:
            "Product rule":
                jump tutorial_product
            "Quotient rule":
                jump tutorial_quotient
            "Chain rule":
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