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
    tutorials = [
        ("tutorial_product", _("Product Rule")),
        ("tutorial_quotient", _("Quotient Rule")),
        ("tutorial_chain", _("Chain Rule")),
        ]
    
init python:
    mp = MultiPersistent("MTH.TeachingMode")

screen tutorials:

    side "c r":
        area (250, 40, 548, 400)

        viewport:
            yadjustment adj
            vbox:
                for label, name in tutorials:
                    button:
                        action Return(label)
                        left_padding 20
                        xfill True
                        hbox:
                            text name style "button_text" min_width 420
                null height 20
                textbutton _("That's enough for now."):
                    xfill True
                    action Return(False)


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
                $ mp.save()
                return
                
            "Student":
                $ mp.option = "Student"
                $ mp.modeSelected = True
                $ mp.save()
                return
    
label start:
    
    $ tutorials_first_time = True
    
    s "Hi! My name is Senpai, and I'd like to welcome you to mth dervaderv tutorial."
    s "In this tutorial, we'll teach you how to do the Product Rule, Quotient Rule, and Chain Rule, so you can practice these dervadervs on your own."
    
    if(mp.option == "Teacher"):
        jump tutorials
    else:
        s "You cannot use this yet."
        jump end
    
    
    
label tutorials:

    $ tutorials_adjustment = ui.adjustment()

    if tutorials_first_time:
        $ s(_("What would you like to see?"), interact=False)
    else:
        $ s(_("Is there anything else you'd like to see?"), interact=False)

    $ tutorials_first_time = False

    call screen tutorials(adj=tutorials_adjustment)

    if _return is False:
        jump end

    call expression _return

    jump tutorials

label end:
    
    s "..."
    s "Thank you for viewing this tutorial."
    
    s "I will reset this for you."
    $ mp.modeSelected = False
    
    window hide
    
    return
