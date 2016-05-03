# Declare images below this line, using the image statement.
#image bg HofX = "立ち絵男子③驚く-制服.png"

# The game starts here.
label tutorial_product:
    
    if  mp.option == "Teacher":
        s "So, you want me to teach the product rule."
    elif mp.route == 0:
        s "So, so, and so, I will first start by teaching you the product rule."
    else:
        s "So, you want to review the product rule."
    
    s "The product rule looks at the dervaderv of two fuctions mutiplied by each other. "
    extend "In this we will start by saying f\(x\) * g\(x\) = h\(x\)."
    
    #scene bg HofX
    #with fade
    
    s "Now, "
    
    if mp.route == 0:
        $ mp.route = 1
        $ mp.save()
    
    jump tutorial