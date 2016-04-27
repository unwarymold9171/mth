# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")

init python:
    tutorials = [
        ("tutorial_playing", _("User Experience"), "6.10.0"),
        ("tutorial_dialogue", _("Writing Dialogue"), "6.10.0"),
        ("tutorial_images", _("Adding Images"), "6.10.0"),
        ]
    
screen tutorials:

    side "c r":
        area (250, 40, 548, 400)

        viewport:
            yadjustment adj
            mousewheel True
            vbox:
                for label, name, ver in tutorials:
                    button:
                        action Return(label)
                        left_padding 20
                        xfill True
                        hbox:
                            text name style "button_text" min_width 420
                            text ver style "button_text"
                null height 20
                textbutton _("That's enough for now."):
                    xfill True
                    action Return(False)
        bar adjustment adj style "vscrollbar"


# The game starts here.
label start:

    e "You've created a new Ren'Py game."
    #stuff
    e "Once you add a story, pictures, and music, you can release it to the world!"
    $ tutorials_adjustment = ui.adjustment()
    call screen tutorials(adj=tutorials_adjustment)

    return
