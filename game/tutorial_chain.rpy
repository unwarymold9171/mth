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
    
    #explation of chain rule, using photos of whiteboards as backrounds
    
    s "The chain rule is used when you need to take the dervaderv of a function of a function, such as \(x + 1\)^2"
    s "The chain rule says that if f\(x\) = g\(h\(x\)\), then f'\(x\) = g'\(h\(x\)\) * h'\(x\)"
    
    #practice problem with answers
    
    #additional explanation of incorrect answers
    
    if mp.route == 2:
        $ mp.route = 3
        $ mp.save()
    
    jump tutorial
