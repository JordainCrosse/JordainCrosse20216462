

# Create a variable to control the loop.
keep_going = 'y'

while keep_going == 'y': 

# Assigning User input to variables

    sales_num = int(input('enter sales person number: '))
    sales = int(input('enter sales amount: '))
    Class = int(input('enter class: '))

# A if statement is used to determine whether the user input meets the criteria for class 1
# if the criteria is meet it will print the saleperson number and the commission

    if Class == 1:
        if sales <= 1000:
            print('The salesperson number is: ' , sales_num , ' and the Commission is ', '$', 0.06 * sales)
        elif 1000 < sales <= 2000:

            print('The salesperson number is: ' , sales_num , ' and the Commission is ', '$', 0.07 * sales)
        else:

            print('The salesperson number is: ' , sales_num , ' and the Commission is ', '$', 0.1 * sales)
    elif Class == 2:

# An else if statement is used to determine whether the user input meets the criteria for class 2
# if the criteria is meet it will print the saleperson number and the commission

        if sales <= 1000:
            print('The salesperson number is: ' , sales_num , ' and the Commission is ', '$', 0.04 * sales)
        else:
            print('The salesperson number is: ' , sales_num , ' and the Commission is ', '$', 0.06 * sales)
    elif Class == 3:

# An else if statement is used to determine whether the user input meets the criteria for class 3
# if the criteria is meet it will print the saleperson number and the commission

        print('The salesperson number is: ' , sales_num , ' and the Commission is ', '$',  0.045 * sales)
    else:

# error message

        print('Incorrect Value')


    # User prompt to see if the user wants to do another calculation the program will loop if the user input is 'y' else it will terminate.
    keep_going = input('Do you want to calculate another ' + \
                       'commission (Enter y for yes): ')
