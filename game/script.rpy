##################################################
# TODO:                                          #
#       create routes                            #
#       implement student vs teacher             #
#       Fix atend of project:                    #
##################################################

init python:
    mp = MultiPersistent("MTH.TeachingMode")

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg lecturehall = im.FactorScale("lecturehall.jpg", .75)
image bg dorm = "Dorm4.png"
image bg dorm night = "Dorm9.png"
image bg library = "library.png"
image bg cafe = im.FactorScale("uncle_mugen_cafe_day.jpg", .75)

image scot = "立ち絵男子①ノーマル-制服.png"
image william = "立ち絵男子③ノーマル-制服.png"
image william happy = "立ち絵男子③喜-制服.png"
image willaim happy2 = "立ち絵男子③楽-制服.png"
image william questioning = "立ち絵男子③困る-制服.png"
image william surprised = "立ち絵男子③驚く-制服.png"

# Declare characters used by this game.
define textless = Character('', color="#000000")
define s = Character("[mp.sName]", color="#c8ffc8")
define p = Character("[mp.playerName]")

label swapMode:
        if(mp.option == "Student"): 
            $ mp.option = "Teacher" 
            $ mp.save()
        else: 
            $ mp.option = "Student"
            $ mp.save()
        $ mp.route = 0
        call screen preferences()
        
label reset:
    
    "Reseting modeSelected"
    $ mp.modeSelected = False
    $ mp.save()
    
label start:
    
    $ tutorials_first_time = True
    
    scene bg lecturehall
    with fade
    
    if mp.route == 0 or mp.option == "Teacher":
        if mp.route == 0:
            $ mp.playerName = renpy.input("What is your name?","",None,'{}',25,None,None)
            $ mp.playerName = mp.playerName.strip()
            if not mp.playerName:
                $ mp.playerName = "Kōhai"
            if mp.playerName.lower() == "your name":
                $ mp.playerName = mp.sName
            if mp.playerName == "Kouhai":
                $ mp.playerName = "Kōhai"
            if mp.playerName.lower() == "lenny face":
                $ mp.playerName = u"\u0028\u00B0\u0361 \u035C\u0296\u00B0\u0361\u0029"
            $ mp.save()
        else:
            $ mp.playerName = "Teacher"
            $ mp.save()
        
        
        s "Hi! My name is [mp.sName], and I'd like to welcome you to mth dervaderv tutorial."
        
        if mp.route == 0:
            s "What is your name?" 
            p "My name is [mp.playerName]."
        
        s "Okay, [mp.playerName]. In this tutorial, we'll teach the Product Rule, Quotient Rule, and Chain Rule, so you can practice these dervadervs on your own."
    else:
        s "Welcome back, [mp.playerName]. "
        if mp.route == 1:
            extend "I have so far taught you the Product Rule"
        elif mp.route == 2:
            extend "I have so far taught you the Product Rule and the Quotient Rule"
        elif mp.route == 3:
            extend "I have so far taught you all three of the rules"
    
    jump tutorial
    
label tutorial:
    
    if tutorials_first_time:
        $ s(_("What would you like to see?"), interact=False)
    else:
        $ s(_("Is there anything else you'd like to see?"), interact=False)
    
    $ tutorials_first_time = False
    
    if mp.route == 0:
        if mp.playerName.lower() == "kōhai":
            menu:
                "Why are you noticing me?":
                    jump noticeMeSenpai
                "Something new":
                    jump tutorial_product
                "That's enough for now.":
                    jump end
        menu:
            "Something new":
                jump tutorial_product
            "That's enough for now.":
                jump end
    elif mp.route == 1:
        if mp.playerName.lower() == "kōhai":
            menu:
                "Why are you noticing me?":
                    jump noticeMeSenpai
                "Product rule":
                    jump tutorial_product
                "Something new":
                    jump tutorial_quotient
                "That's enough for now.":
                    jump end
        menu:
            "Product rule":
                jump tutorial_product
            "Something new":
                jump tutorial_quotient
            "That's enough for now.":
                jump end
    elif mp.route == 2:
        if mp.playerName.lower() == "kōhai":
            menu:
                "Why are you noticing me?":
                    jump noticeMeSenpai
                "Product rule":
                    jump tutorial_product
                "Quotient rule":
                    jump tutorial_quotient
                "Something new":
                    jump tutorial_chain
                "That's enough for now.":
                    jump end
        menu:
            "Product rule":
                jump tutorial_product
            "Quotient rule":
                jump tutorial_quotient
            "Something new":
                jump tutorial_chain
            "That's enough for now.":
                jump end
    else:
        if mp.playerName.lower() == "kōhai":
            menu:
                "Why are you noticing me?":
                    jump noticeMeSenpai
                "Product rule":
                    jump tutorial_product
                "Quotient rule":
                    jump tutorial_quotient
                "Chain rule":
                    jump tutorial_chain
        menu:
            "Product rule":
                jump tutorial_product
            "Quotient rule":
                jump tutorial_quotient
            "Chain rule":
                jump tutorial_chain
            "That's enough for now.":
                jump end
                
label noticeMeSenpai:
    
    
    
    jump tutorial

label end:
    
    s "..."
    s "Thank you for viewing this tutorial."
    
    window hide
    
    return