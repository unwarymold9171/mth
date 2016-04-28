# The game starts here.
label tutorial_product:
    
    if  mp.option == "Teacher":
        s "So, you want me to teach the product rule."
    elif mp.route == 0:
        s "Okay I will first start by teaching you the product rule"
    
    s "Once you add a story, pictures, and music, you can release it to the world!"
    
    $ mp.route = 1
    $ mp.save()
    
    jump tutorial