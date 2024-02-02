def main():
    print("this is monthly loan payment calculator ")
    print("")

    
    principal = float(input("input the loan amount: "))
    apr = float(input("input the annual intrest rate: "))
    years = int(input("input amount of years: "))


    monthly_intrest_rate = apr / 1200
    amount_of_months = years *12
    monthly_payment = principal * monthly_intrest_rate / (1-(1 + monthly_intrest_rate) **(-amount_of_months))



    print("the monthly payment for this loan is : " + str(monthly_payment))

main()    