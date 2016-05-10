# Declare images below this line, using the image statement.
image bg blank = im.FactorScale("ProductWhiteBoard/DSCF1829.JPG", .281)
image bg HofX = im.FactorScale("ProductWhiteBoard/DSCF1830.JPG", .281)
image bg HofXlim = im.FactorScale("ProductWhiteBoard/DSCF1833.JPG", .281)
image bg FofXstarGofXlim = im.FactorScale("ProductWhiteBoard/DSCF1834.JPG", .281)
image bg FofXstarGofXlimPlusZero = im.FactorScale("ProductWhiteBoard/DSCF1835.JPG", .281)
image bg FofXstarGofXlimPlusZeroSymplefied = im.FactorScale("ProductWhiteBoard/DSCF1837.JPG", .281)
image bg LotsOfSymplificationAndWhatHasHappenedToTheseVerableNames = im.FactorScale("ProductWhiteBoard/DSCF1838.JPG", .281)
image bg LotsOfSymplificationAndMoreSymplificationAndMakingMoreLongVerableNamesAgain = im.FactorScale("ProductWhiteBoard/DSCF1839.JPG", .281)
image bg FingDoneWithTheseLongNamesForThePicturesOfAWhiteBoardProvingTheProductRuleFinalPicture = im.FactorScale("ProductWhiteBoard/DSCF1840.JPG", .281)
image bg Practice1 = im.FactorScale("ProductWhiteBoard/DSCF1841.JPG", .281)
image bg Practice2 = im.FactorScale("ProductWhiteBoard/DSCF1843.JPG", .281)
image bg Practice3 = im.FactorScale("ProductWhiteBoard/DSCF1844.JPG", .281)
image bg Practice4 = im.FactorScale("ProductWhiteBoard/DSCF1845.JPG", .281)

# The game starts here.
label tutorial_product:
    
    if  mp.option == "Teacher":
        s "So, you want me to teach the product rule."
    elif mp.route == 0:
        s "So, so, and so, I will first start by teaching you the product rule."
    else:
        s "So, you want to review the product rule."
    
    scene bg blank
    with fade
    
    s "The product rule looks at the dervaderv of two fuctions mutiplied by each other. "
    extend "In this we will start by saying f\(x\)\u205F*\u205Fg\(x\) = h\(x\)."
    
    scene bg HofX
    with dissolve
    
    
    s "Now, let's look at this with the formal definition."
    
    scene bg HofXlim
    with dissolve
    
    s "Now that we have it in this form we can change it from h\(x\) we can change it back to f\(x\)\u205F*\u205Fg\(x\)."
    
    scene bg FofXstarGofXlim
    with dissolve
    
    s "From here,  we need to add a special form of zero. This will be in the form of -\u205Ff\(x\)\u205F*\u205Fg\(x\u205F+\u205F\u0394x\)\u205F+\u205Ff\(x\)\u205F*\u205Fg\(x\u205F+\u205F\u0394x\) all over \u0394x."
    
    scene bg FofXstarGofXlimPlusZero
    with dissolve
    
    s "Now this can be symplified down changing it to \[f\(x\u205F+\u205F\u0394x\)\u205F-\u205Ff\(x\)\]\u205F*\u205Fg\(x\u205F+\u205F\u0394x\)\u205F+\u205Ff\(x\)\u205F*\u205F\[g\(x\u205F+\u205F\u0394x\)\u205F-\u205Fg\(x\)\] all over \u0394x."
    
    scene bg FofXstarGofXlimPlusZeroSymplefied
    with dissolve
    
    s "From here, because when taking the limit of two things being added togeather we can split it into lim\(\[f\(x\u205F+\u205F\u0394x\)\u205F-\u205Ff\(x\)\]/\u0394x\u205F*\u205Fg\(x\u205F+\u205F\u0394x\)\)\u205F+\u205Flim\(f\(x\)\u205F*\u205F\[g\(x\u205F+\u205F\u0394x\)\u205F-\u205Fg\(x\)\]/\u0394x\)"
    
    scene bg LotsOfSymplificationAndWhatHasHappenedToTheseVerableNames
    with dissolve
    
    s "Now, we will be lim\(\[f\(x\u205F+\u205F\u0394x\)\u205F-\u205Ff\(x\)\]/\u0394x\u205F\)\u205F*\u205Flim\(\u205Fg\(x\u205F+\u205F\u0394x\)\)\u205F+\u205Flim\(f\(x\)\u205F\)\u205F*\u205Flim\(\u205F\[g\(x\u205F+\u205F\u0394x\)\u205F-\u205Fg\(x\)\]/\u0394x\)"
    
    scene bg LotsOfSymplificationAndMoreSymplificationAndMakingMoreLongVerableNamesAgain
    with dissolve
    
    s "Now that it is in this form, we can see lim\(\[f\(x\u205F+\u205F\u0394x\)\u205F-\u205Ff\(x\)\]/\u0394x\u205F\) and this equals the dervaderve of f\(x\);
       the same goes for lim\(\u205F\[g\(x\u205F+\u205F\u0394x\)\u205F-\u205Fg\(x\)\]/\u0394x\) equaling the dervaderve of g\(x\). 
       There is also lim\(\u205Fg\(x\u205F+\u205F\u0394x\) and this just equals g\(x\)."
    
    scene bg FingDoneWithTheseLongNamesForThePicturesOfAWhiteBoardProvingTheProductRuleFinalPicture
    with dissolve
    
    s "And with this we can see that \(f\(x\)g\(x\)\)' = f'\(x\)\u205F*g\(x\)\u205F+\u205Ff\(x\)\u205F*g'\(x\)"
    
    scene bg lecturehall
    with fade 
    
    if mp.route == 0:
        s "Okay, now onto practice the problems."
        jump practice_product
    elif mp.route == 10:
        $ s(_("Would you like me to give practice problems?"), interact=False)
        menu:
            "Yes":
                jump practice_product
            "No":
                jump end_product
    else:
        $ s(_("Would you like me to go back over the practice problems?"), interact=False)
        menu:
            "Yes":
                jump practice_product
            "No":
                jump end_product
                
label practice_product:
    
    $ productTWrong = 0
    $ productCWrong = 0
    
    s "Okay, I will write them down now."
    
    scene bg Practice1
    with fade
        
    s "Here are three practice problems to try out. "
    extend "Try them out for yourself."
    
label practice_product1:
    $ s(_("What do you think the answer for A is?"), interact=False)
    menu:
        "Yes":
            s "Correct!"
            scene bg Practice2
            with dissolve
            $ productCWrong = 0
            jump practice_product2
        "No":
            s "Wrong try again"
            $ productTWrong += 1
            $ productCWrong += 1
            jump practice_product1

label practice_product2:
    $ s(_("What do you think the answer for B is?"), interact=False)
    menu:
        "Yes":
            s "Correct!"
            scene bg Practice3
            with dissolve
            $ productCWrong = 0
            jump practice_product3
        "No":
            s "Wrong try again"
            $ productTWrong += 1
            $ productCWrong += 1
            jump practice_product2
                
label practice_product3:
    $ s(_("What do you think the answer for C is?"), interact=False)
    menu:
        "Yes":
            s "Correct!"
            scene bg Practice4
            with dissolve
            $ productCWrong = 0
            jump practice_product4
        "No":
            s "Wrong try again"
            $ productTWrong += 1
            $ productCWrong += 1
            jump practice_product3

label practice_product4:
    
    s "You got [productTWrong] wrong answers."
    
    scene bg lecturehall
    with fade 
    
    if productTWrong == 0 and mp.option == "Student":
        s "I think you are definitely ready for the next lesson."
        jump end_product
    elif productTWrong <= 3 and mp.option == "Student":
        s "I think your ready for the next lesson."
        jump end_product
    elif productTWrong <= 6 and mp.option == "Student":
        s "I think you should practice more before the next lesson."
        jump end_product
    elif mp.option == "Student":
        s "You need more practice before going onto the next lesson."
        jump practice_product
    elif productTWrong < 0:
        s "How come you missed these problems?"
        jump end_product
    else:
        s "I have no clue what to say, you broke the system."
        
label end_product:
    
    if mp.route == 0:
        $ mp.route = 1
        $ mp.save()
    
    jump tutorial