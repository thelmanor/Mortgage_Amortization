"""
Name: Thelma Nora
Lab No: Lab 4
Description: Modifications added to the mortgage calculator from Lab 3. It is a program that asks for information
            about a mortgage loan and prints the amortized schedule.
Program Name: MortgageCalculator
Date: 09/16/2019
"""
import time

x = 0
y = 0
z = 0


# function to receive loan amount input from user
def amt():
    loan_amt = input("Please enter your mortgage loan amount (in dollars):\t")
    # if-else statement to ensure that loan amount input is a valid entry
    if loan_amt.isnumeric():
        global x
        x = float(loan_amt)
        print("valid entry: ", x)
    else:
        print(" You have made an invalid entry, please try again")
        amt()
    return x


# function to receive loan term input from user and convert input from years to months
def term():
    loan_term = input("Please enter the term of the loan (in years):\t")
    # validation statement to ensure that loan term input is a valid entry
    if loan_term.isnumeric() and 10 <= int(loan_term) <= 40:
        global y
        y = 0
        y = int(loan_term)
        y = (y * 12)
        print("valid entry: ", y)
    else:
        print(" You have made an invalid entry, please try again")
        term()
    return y


# function to receive loan rate input from user and convert input from yearly rate to monthly rate
def rate():
    int_rate = input("Please enter the interest rate (in %):\t")
    # validation statement to ensure that loan rate input is a valid entry
    try:
        int_rate.isnumeric()
        if 10 >= float(int_rate) > 0:
            int_rate = float(int_rate)
            global z
            z = float(int_rate)
            z = (z / 12) / 100
            print("valid entry: ", int_rate)
        else:
            print(" You have made an invalid entry, please try again")
            rate()
    except ValueError:
        print(" You have made an invalid entry, please try again")
        rate()
    return z


# function to calculate monthly payment
def monthlyPayment():
    loan = amt()
    months = term()
    interest = rate()
    pyt = float(str(round(loan * (interest * (1 + interest) ** months) / ((1 + interest) ** months - 1), 2)))
    print("Your monthly payment will be :  $%0.2f" % pyt)
    calcPaymentAgain()
    return pyt


# function to ask user if they would like to calculate another monthly payment
def calcPaymentAgain():
    again = input("Would you like to calculate another mortgage?, Please enter 'Y' or 'N'")
    while again.upper() == "Y":
        monthlyPayment()
    if again.upper() == "N":
        exit(0)
    else:
        print('You have entered an invalid response, please try again ', '\n')
        calcPaymentAgain()


# This function allows user to calculate monthly payment and print out an amortized statement,
# This function also creates a timestamped file each time a statement is printed
def statement():
    loan = amt()
    months = term()
    interest = rate()
    monthlyPay = float(str(round(loan * (interest * (1 + interest) ** months) / ((1 + interest) ** months - 1), 2)))
    payment = monthlyPay
    month = 0
    monthlyInterest = round((interest * loan), 2)
    principal = round((payment - monthlyInterest), 2)
    balance = loan - principal
    total_interest_paid = 0
    currentTime = time.localtime()  # function to generate local time
    currentTimeString = time.strftime("%m %d %H %M %S", currentTime)  # convert local time generated to string
    file = 'statement{}.txt'.format(currentTimeString)  # append time string generated to file name
    printout = open(file, 'w')  # open a file

    # print statement header to the file
    printout.writelines("Month \t Principal \t Interest\t Payment\t Balance\n")
    printout.writelines("----- \t -------- \t--------- \t -------\t--------\n")

    # print statement header on console
    print("Payment Month", "\t\t\t", "Principal Paid", "\t\t", "Interest Paid", "\t\t\t", "Monthly Payment",
          "\t\t\t",
          "Mortgage Balance")
    print("-------------", "\t\t\t", "--------------", "\t\t", "-------------", "\t\t\t", "----------------"
                                                                                          " \t\t\t----------------")

    # loop to generate monthly principal paid, monthly interest paid, monthly balance and month of payment
    while balance > 0:
        monthlyInterest = round((interest * balance), 2)
        principal = round((payment - monthlyInterest), 2)
        balance = round((balance - principal), 2)
        month += 1
        total_interest_paid += monthlyInterest

        # print statement to print monthly principal paid, monthly interest paid, monthly balance and month of payment
        if balance > 0:  # for balance over 0
            print("{0:<25}{1:<20,.2f} {2:<20,.2f} {3:<20,.2f} {4:<20,.2f}".format(month, principal, monthlyInterest,
                                                                                  payment, balance))
            printout.writelines("{0:<10} {1:<10,.2f} {2:<10,.2f} {3:<10,.2f} {4:<10,.2f}\n"
                                .format(month, principal, monthlyInterest, payment, balance))
        else:
            balance = 0  # for balance below 0 or negative balance
            print("{0:<25}{1:<25,.2f} {2:<25,.2f} {3:<25,.2f}".format(month, principal, monthlyInterest, balance))
            printout.writelines("{0:<10} {1:<10,.2f} {2:<10,.2f} {3:<10,.2f} {4:<10,.2f}\n"
                                .format(month, principal, monthlyInterest, payment, balance))

    printout.close()  # close file

    #  calculation of total interest paid
    print("Total interest paid will be:  ${0:,.2f}".format((payment * month) - loan))
    #  print total principal paid
    print("Total principal paid will be:  ${0:,.2f}".format(loan))
    printAnotherStatement()


# function to ask user if they would like to calculate and print out another amortized statement
def printAnotherStatement():
    again = input("Would you like to print another mortgage statement?, Please enter 'Y' or 'N'")
    while again.upper() == "Y":
        statement()
    if again.upper() == "N":
        exit(0)
    else:
        print('You have entered an invalid response, please try again ', '\n')
        printAnotherStatement()


def main():  # main method used to initiate the program
    print("=" * 150)
    print("$$$$$ Thelma's Mortgage Calculator")
    print("$$$$$ This program calculates your monthly mortgage loan payments as well as printing out an"
          "amortization schedule")
    print("$$$$$ If you would like to use the Mortgage Payment Calculator only, please enter 'MPC' when prompted")
    print("$$$$$ If you would like to use the Mortgage Payment Calculator along with the amortization schedule,"
          " please enter 'AS' when prompted")
    print("=" * 150)
    start_program = input("What would you like to do with the program?\n")
    if start_program.upper() == "MPC":
        monthlyPayment()
    elif start_program.upper() == "AS":
        statement()
    else:
        print('You have entered an invalid response, please try again ', '\n')
        main()


main()
