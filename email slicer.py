def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("input your email address: ")

    (username,domain) = email_input.split("@")
    (domain, extention) = domain.split(".")

    print("username:", username)
    print("domain:", domain)
    print("extention:", extention)

main()    