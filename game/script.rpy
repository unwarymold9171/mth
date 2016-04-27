# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define s = Character('Senpai', color="#c8ffc8")

init python:
    tutorials = [
        ("tutorial_product", _("Product Rule")),
        ("tutorial_quotient", _("Quotient Rule")),
        ("tutorial_chain", _("Chain Rule")),
        ]
    
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
label start:
    
    $ tutorials_first_time = True
    
    s "Hi! My name is Eileen, and I'd like to welcome you to the Ren'Py tutorial."
    s "In this tutorial, we'll teach you the basics of Ren'Py, so you can make games of your own. We'll also demonstrate many features, so you can see what Ren'Py is capable of."
    
    
    $ tutorials_adjustment = ui.adjustment()
    
label tutorials:

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

    return
