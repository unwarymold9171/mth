﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")

# The game starts here.
label product:

    e "You've created a new Ren'Py game."
    #stuff
    e "Once you add a story, pictures, and music, you can release it to the world!"
    $ tutorials_adjustment = ui.adjustment()
    call screen tutorials(adj=tutorials_adjustment)

    return
