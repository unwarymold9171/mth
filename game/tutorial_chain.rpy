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
image bg Practice5 = im.FactorScale("ChainWhiteBoard/DSCF1852.JPG", .281)
image bg Practice6 = im.FactorScale("ChainWhiteBoard/DSCF1853.JPG", .281)
image bg Practice7 = im.FactorScale("ChainWhiteBoard/DSCF1854.JPG", .281)
image bg Practice8 = im.FactorScale("ChainWhiteBoard/DSCF1855.JPG", .281)

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
    s "That means that for \(x + 1\)^2, f\(x\) would be \(x + 1\)^2, g\(x\) would be x^2, and h\(x\) would be \(x + 1\)" 
    s "Thus, h'\(x\) would be \(x + 1\)', or 1, and g'\(h\(x\)\) would be \(\(x + 1\)^2\)', or 2\(x + 1\)" 
    s "Therefor, f'\(x\) would be 1 * 2\(x + 1\), which is just 2\(x + 1\)"
    
    #practice problem with answers
    
    #additional explanation of incorrect answers
    
    if mp.route == 2:
        $ mp.route = 3
        $ mp.save()
    
    jump tutorial
