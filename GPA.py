import time
while True:
    
    print("Hello, I am a program that can help you determine GPA")
    print("Note that this calculator may not be completely accurate, due to differences in the public school system.")
    print("Please refrain from lowercase letters, minuses or pluses, and any other letters.")
    one = input("Class 1: ")
    two = input("Class 2: ")
    three = input("Class 3: ")
    four = input("Class 4: ")
    five = input("Class 5: ")
    six = input("Class 6: ")
    
    def ClassOne():
        gradeOne = 0
        if one == "A":
            gradeOne = gradeOne + 4
        elif one == "B":
            gradeOne = gradeOne + 3
        elif one == "C":
            gradeOne = gradeOne + 2
        elif one == "D":
            gradeOne = gradeOne + 1
        elif one == "F":
            gradeOne = gradeOne + 0
        else:
            print ("Try again.")
        return gradeOne
    one = ClassOne()
    
    def ClassTwo():
        gradeTwo = 0
        if two == "A":
            gradeTwo = gradeTwo + 4
        elif two == "B":
            gradeTwo = gradeTwo + 3
        elif two == "C":
            gradeTwo = gradeTwo + 2
        elif two == "D":
            gradeTwo = gradeTwo + 1
        elif two == "F":
            gradeTwo = gradeTwo + 0
        else:
            print ("Try again.")
        return gradeTwo
            
    two = ClassTwo()        
    
    def ClassThree():
        gradeThree = 0
        if three == "A":
            gradeThree = gradeThree + 4
        elif three == "B":
            gradeThree = gradeThree + 3
        elif three == "C":
            gradeThree = gradeThree + 2
        elif three == "D":
            gradeThree = gradeThree + 1
        elif three == "F":
            gradeThree = gradeThree + 0
        else:
            print ("Try again.")
        return gradeThree
    
    three = ClassThree()    
        
    def ClassFour():
        gradeFour = 0
        if four == "A":
            gradeFour = gradeFour + 4
        elif four == "B":
            gradeFour = gradeFour + 3
        elif four == "C":
            gradeFour = gradeFour + 2
        elif four == "D":
            gradeFour = gradeFour + 1
        elif four == "F":
            gradeFour = gradeFour + 0
        else:
            print ("Try again.")
        return gradeFour
            
    four = ClassFour()
            
    def ClassFive():
        gradeFive = 0
        if five == "A":
            gradeFive = gradeFive + 4
        elif five == "B":
            gradeFive = gradeFive + 3
        elif five == "C":
            gradeFive = gradeFive + 2
        elif five == "D":
            gradeFive = gradeFive + 1
        elif five == "F":
            gradeFive = gradeFive + 0
        else:
            print ("Try again.")
        return gradeFive
            
    five = ClassFive()
            
    def ClassSix():
        gradeSix = 0
        if six == "A":
            gradeSix = gradeSix + 4
        elif six == "B":
            gradeSix = gradeSix + 3
        elif six == "C":
            gradeSix = gradeSix + 2
        elif six == "D":
            gradeSix = gradeSix + 1
        elif six == "F":
            gradeSix = gradeSix + 0
        else:
            print ("Try again.")
        return gradeSix
    
    six = ClassSix()
    GPA = 0
    GPA = one + two + three + four + five + six
    FinalGPA = GPA / 6
    print(FinalGPA)
    time.sleep(1)
    print("Rebooting.")
    time.sleep(3)
    
    
    
