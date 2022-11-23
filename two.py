'''
    display ft will serve as a canvas
'''

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

def user_choice():
    #variables

    #Initial values
    choice = 'wrong'
    acceptable_range = range(0,10)
    within_range = False

    '''
        Two cdt to check
        DIGIT OR WITHIN_RANGE == False
    '''

    while choice.isdigit() == False or within_range==False:

        choice = input("Pls Enter a number (0 - 9): ")

        #Digit Check
        if choice.isdigit() == False:
            print("Sorry that is not a digit")

        # Range Check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
                print(
                    "well done"
                )

            else:
                print("out of range")
                within_range = False

    return  int(choice)




