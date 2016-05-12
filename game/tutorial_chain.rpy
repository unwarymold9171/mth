#######################################
#               TO-DO:                #
#       browse dank memes             #
#       git gud                       #
#######################################

# Declare images below this line, using the image statement.
image bg ChainDemo1 = im.FactorScale("ChainWhiteBoard/DSCF1847.JPG", .281)
image bg ChainDemo2 = im.FactorScale("ChainWhiteBoard/DSCF1848.JPG", .281)
image bg ChainDemo3 = im.FactorScale("ChainWhiteBoard/DSCF1849.JPG", .281)
image bg ChainDemo4 = im.FactorScale("ChainWhiteBoard/DSCF1850.JPG", .281)
image bg ChainDemo5 = im.FactorScale("ChainWhiteBoard/DSCF1851.JPG", .281)
image bg Practice5 = im.FactorScale("ChainWhiteBoard/DSCF1872.JPG", .281)
image bg Practice6 = im.FactorScale("ChainWhiteBoard/DSCF1873.JPG", .281)
image bg Practice7 = im.FactorScale("ChainWhiteBoard/DSCF1875.JPG", .281)
image bg Practice8 = im.FactorScale("ChainWhiteBoard/DSCF1876.JPG", .281)

# The route starts here.
label tutorial_chain:

    if  mp.option == "Teacher":
        s "So, you want me to teach the chain rule."
    elif mp.route == 0:
        s "So, I will first start by teaching you the chain rule."
    else:
        s "So, you want to review the chain rule."
    
    #explation of chain rule, using photos of whiteboards as backrounds
    
    scene bg ChainDemo1
    with fade
    s "The chain rule is used when you need to take the dervaderv of a function of a function, such as \(x + 1\)^2"
    scene bg ChainDemo2
    with dissolve
    s "The chain rule says that if f\(x\) = g\(h\(x\)\), then f'\(x\) = g'\(h\(x\)\) * h'\(x\)"
    scene bg ChainDemo3
    with dissolve
    s "That means that for \(x + 1\)^2, f\(x\) would be \(x + 1\)^2, g\(x\) would be x^2, and h\(x\) would be \(x + 1\)" 
    scene bg ChainDemo4
    with dissolve
    s "Thus, h'\(x\) would be \(x + 1\)', or 1, and g'\(h\(x\)\) would be \(\(x + 1\)^2\)', or 2\(x + 1\)" 
    scene bg ChainDemo5
    with dissolve
    s "Therefor, f'\(x\) would be 1 * 2\(x + 1\), which is just 2\(x + 1\)"
    scene bg ChainDemo1
    with dissolve
    
    #practice problem with answers
    
    if mp.route == 0:
        s "Okay, now onto practice the problems."
        jump practice_product
    elif mp.route == 10:
        $ s(_("Would you like me to give practice problems?"), interact=False)
        menu:
            "Yes":
                jump chain_practice
            "No":
                jump end_chain
    else:
        $ s(_("Would you like me to go back over the practice problems?"), interact=False)
        menu:
            "Yes":
                jump chain_practice
            "No":
                jump end_chain
    
label chain_practice:
    
    $ chainTWrong = 0
    $ chainCWrong = 0
    
    s "Okay, I will write them down now."
    
    scene bg Practice5
    with fade
        
    s "Here are three practice problems to try out. "
    extend "Try them out for yourself."
    
label chain_practice1:
    
    s "Here are the practice problems"
    scene bg Practice5
    with dissolve
label chain_practice2:
    $ s(_("What do you think the answer for the A is?"), interact=False)
    menu:
        "8tan^4(x)sec^2(x)":
            s "Wrong try again"
            $ chainTWrong += 1
            $ chainCWrong += 1
            jump chain_practice2
        "4tan^3(x)sec^2(x)":
            s "Correct!"
            scene bg Practice6
            with dissolve
            $ chainCWrong = 0
        "4sec^6(x)":
            s "Wrong try again"
            $ chainTWrong += 1
            $ chainCWrong += 1
            jump chain_practice2
        "4tan^3(x)":
            s "Wrong try again"
            $ chainTWrong += 1
            $ chainCWrong += 1
            jump chain_practice2
label chain_practice3:
    $ s(_("What do you think the answer for B is?"), interact=False)
    menu:
        "-sin(x^3+3x^2+4x)(3x^2+6x+4)(6x+6)":
            s "Wrong try again"
            $ chainTWrong += 1
            $ chainCWrong += 1
            jump chain_practice3
        "sin(x^3+3x^2+4x)(3x^2+6x+4)(6x+6)":
            s "Wrong try again"
            $ chainTWrong += 1
            $ chainCWrong += 1
            jump chain_practice3
        "-sin(x^3+3x^2+4x)(3x^2+6x+4)":
            s "Correct!"
            scene bg Practice7
            with dissolve
            $ chainCWrong = 0
        "sin(x^3+3x^2+4x)(3x^2+6x+4)":
            s "Wrong try again"
            $ chainTWrong += 1
            $ chainCWrong += 1
            jump chain_practice3
        "-sin(x^3+3x^2+4x)":
            s "Wrong try again"
            $ chainTWrong += 1
            $ chainCWrong += 1
            jump chain_practice3
label chain_practice4:
    $ s(_("What do you think the answer for C is?"), interact=False)
    menu:
        "((x^3+7x)^4)cos(x^3+5e^x)- 4(x^3+7x)^3(3x^2+7)sin(x^3+5e^x)*(3x^2+5e^x)":
            s "Wrong try again"
            $ chainTWrong += 1
            $ chainCWrong += 1
            jump chain_practice4
        "4(x^3+7x)^3(3x^2+7)cos(x^3+5e^x)- (x^3+7x)^4sin(x^3+5e^x)(3x^2+5e^x)":
            s "Correct!"
            scene bg Practice8
            with dissolve
            $ chainCWrong = 0
        "4(x^3+7x)^3(3x^2+7)cos(x^3+5e^x)+ (x^3+7x)^4sin(x^3+5e^x)(3x^2+5e^x)":
            s "Wrong try again"
            $ chainTWrong += 1
            $ chainCWrong += 1
            jump chain_practice4
        "-4(x^3+7x)*(3x^2+7)*(sin(x^3+5e^x))*(3x^2+5e^x)":
            s "Wrong try again"
            $ chainTWrong += 1
            $ chainCWrong += 1
            jump chain_practice4
            
    s "You got [chainTWrong] wrong answers."
    
    scene bg lecturehall
    with fade 
    
    if chainTWrong == 0 and mp.option == "Student":
        s "I think you are definitely ready for the next lesson."
        jump end_chain
    elif chainTWrong <= 3 and mp.option == "Student":
        s "I think your ready for the next lesson."
        jump end_chain
    elif chainTWrong <= 6 and mp.option == "Student":
        s "I think you should practice more before the next lesson."
        jump end_chain
    elif mp.option == "Student":
        s "You need more practice before going onto the next lesson."
        jump chain_practice1
    elif chainTWrong == 0:
        s "Cool, I guess onto another lesson."
        jump end_chain
    elif chainTWrong > 0:
        s "How come you missed these problems?"
        jump end_chain
    else:
        s "I have no clue what to say, you broke the system."
    
    #additional explanation of incorrect answers
    
label end_chain:
    
    scene bg lecturehall
    with fade
    
    if mp.route == 2:
        $ mp.route = 3
        $ mp.save()

    jump tutorial
