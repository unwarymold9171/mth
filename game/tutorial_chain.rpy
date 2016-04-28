####################################################################################
#               TO-DO:
#       browse dank memes
#       add text n stuff
#33333333333333333333333333333333333333333333333333333333333333333333333333333333333

# The game starts here.
label tutorial_chain:

    s "You've created a new Ren'Py game."
    #stuff
    s "Once you add a story, pictures, and music, you can release it to the world!"
    
    if  mp.option == "Student" and mp.route == 1:
        $ mp.route = 2
        $ mp.save()
        jump tutorial_quotient

    
    #text n stuff
    
    
    $ mp.route = 3
    $ mp.save()
    
    jump tutorial
