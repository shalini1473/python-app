def main():
    print("this program converts US dollars to pounds sterling")
    print()

    dollars = eval(input("enter amount in dollars: "))

    pounds = convert_to_pounds(dollars)

    print("that is", pounds, "pounds.")


convert_to_pounds = lambda dollars : dollars * 0.82   

main()