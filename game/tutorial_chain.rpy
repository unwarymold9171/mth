#######################################
#               TO-DO:                #
#       browse dank memes             #
#       git gud                       #
#######################################

# The route starts here.
label tutorial_chain:

    if  mp.option == "Teacher":
        s "So, you want me to teach the chain rule."
    elif mp.route == 0:
        s "So, I will first start by teaching you the chain rule."
    else:
        s "So, you want to review the chain rule."
    
    s "Once you add a story, pictures, and dank memes, you can release it to the world!"
    s "lel text and stuff"
    
    #explation of chain rule, using photos of whiteboards as backrounds
    
    #practice problem with answers
    
    #additional explanation of incorrect answers
    
    if mp.route == 2:
        $ mp.route = 3
        $ mp.save()
    
    jump tutorial
