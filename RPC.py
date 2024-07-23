def rpc():
    while True:
        print("Here is the income portion")
        rentalIncome = float(input("Enter the monthly income: "))
        laundryIncome = float(input("Enter the monthly laundry income: "))
        storageIncome = float(input("Enter the monthly storage income: "))
        miscIncome = float(input("Enter the monthly misc income: "))
        monthlyIncome = rentalIncome + laundryIncome + storageIncome + miscIncome
        print("monthly income: ", monthlyIncome)

        print("here is the expenses portion: ")
        taxes = float(input("Enter the taxes: "))
        water = float(input("Enter the water bill: "))
        garbage = float(input("Enter the monthly garbage bill: "))
        ElectricGas = float(input("Enter the monthly electric/gas bill: "))
        hoa = float(input("Enter the monthly HOA fee: "))
        lawnCare = float(input("Enter the monthly lawn care fees: "))
        vacancy = float(input("Enter the monthly vacvancy fee: "))
        repairs = float(input("Enter the monthly repairs: "))
        capEx = float(input("Enter the monthly CapEx: "))
        propMgmt = float(input("Enter the Property Management fee: "))
        mortgage = float(input("Enter the Mortgage: "))

        expenses = taxes+water+garbage+ElectricGas+hoa+lawnCare+vacancy+repairs+capEx+propMgmt+mortgage
        print("monthly expenses: ", expenses)

        print("Here is the cash flow portion")
        cashFlow = monthlyIncome+expenses

        print("Monthly cash flow: ", cashFlow)

        annualCashFlow = cashFlow*12

        print("Annual cash flow: ", annualCashFlow)

        print("Here is the cash on cash return portion and ending")
        downPayment = float(input("Enter the down payment: "))
        closingCosts = float(input("Enter the closing costs: "))
        rehabCosts = float(input("Enter the rehab costs: "))
        miscCosts = float(input("Enter the misc costs: "))

        totalInvestment = downPayment+closingCosts+rehabCosts+miscCosts

        print("total investment: ", totalInvestment)

        cashOnCashReturn = annualCashFlow/totalInvestment*100
        print("Your cash on cash return percent is: ",cashOnCashReturn,"%")

        repeat = input("Do you want to caclulate another property? (Y/N): ")
        if repeat.upper() == 'Y':
            rpc()
        elif repeat.upper() == 'N':
            break
        else:
            print("invalid input.")

        return monthlyIncome, expenses, annualCashFlow, cashFlow, totalInvestment, cashOnCashReturn

rpc()

