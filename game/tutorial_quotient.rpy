﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image bg QuotientDemo1 = im.FactorScale("QuotientWhiteBoard/DSCF1856.JPG", .281)
image bg QuotientDemo2 = im.FactorScale("QuotientWhiteBoard/DSCF1857.JPG", .281)
image bg QuotientDemo3 = im.FactorScale("QuotientWhiteBoard/DSCF1858.JPG", .281)
image bg QuotientDemo4 = im.FactorScale("QuotientWhiteBoard/DSCF1859.JPG", .281)
image bg QuotientDemo5 = im.FactorScale("QuotientWhiteBoard/DSCF1860.JPG", .281)
image bg QuotientDemo6 = im.FactorScale("QuotientWhiteBoard/DSCF1861.JPG", .281)
image bg QuotientDemo7 = im.FactorScale("QuotientWhiteBoard/DSCF1862.JPG", .281)
image bg Practice9 = im.FactorScale("QuotientWhiteBoard/DSCF1864.JPG", .281)
image bg Practice10 = im.FactorScale("QuotientWhiteBoard/DSCF1865.JPG", .281)
image bg Practice11 = im.FactorScale("QuotientWhiteBoard/DSCF1866.JPG", .281)
image bg Practice12 = im.FactorScale("QuotientWhiteBoard/DSCF1867.JPG", .281)

# The game starts here.
label tutorial_quotient:

    if  mp.option == "Teacher":
        s "So, you want me to teach the quotient rule."
    elif mp.route == 1:
        s "Okay I will first start by teaching you the quotient rule."
    else:
        s "So, you want to review the quotient rule."
    
    scene bg QuotientDemo1
    with fade
    
    s "The Quotient Rule can be used to take the dervderv of a fraction with two functions over each other such as f(x) = g(x)/u(x)."
    
    scene bg QuotientDemo2
    with dissolve
    
    s "Here you have the function f."
    
    scene bg QuotientDemo3
    with dissolve
    
    s "To set up the Quotient Rule you need to take the top of the fraction and multiply it by the derivative of the bottom. You then subtract that from the bottom multiplied by the derivative of the top, all divided by the bottom squared."
    
    scene bg QuotientDemo4
    with dissolve
    
    s "Once you have done that, you will need to make it so that the fraction can be simplified. In order to do this, you will need to expand the top and bottom functions."
    
    scene bg QuotientDemo5
    with dissolve
    
    s "Once you have the expanded forms you can start combining like terms."
    
    scene bg QuotientDemo6
    with dissolve
    
    s "You can stop here or continue simplefiing down."
    
    scene bg QuotientDemo7
    with dissolve
    
    s "And this is the final form."
    
   
    s "A simple way to remember the quotient rule is this little ryhme. Low d high, less high d low, and don't forget to square below."
    
    
    
    scene bg lecturehall
    with fade
    jump end_quotient
    
label end_quotient:

    if mp.route == 1:
        $ mp.route = 2
        $ mp.save()
    
    jump tutorial