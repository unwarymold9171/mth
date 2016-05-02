# The game starts here.
label tutorial_product:
    
    if  mp.option == "Teacher":
        s "So, you want me to teach the product rule."
    elif mp.route == 0:
        s "So, so, and so, I will first start by teaching you the product rule."
    else:
        s "So, you want to review the product rule."
    
    s "Once you add a story, pictures, and music, you can release it to the world!"
    
    if mp.route == 0:
        $ mp.route = 1
        $ mp.save()
    
    jump tutorial