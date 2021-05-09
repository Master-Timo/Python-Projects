def general_acronym(user_input_value):
    user_input = user_input_value
    lst = user_input.split(" ")
    st = ""
    for wrd in lst:
        st = st+str(wrd[0]).upper()
    print(st)

def full_initial(user_input_value):
    pass

def sp_acronym(user_input_value):
    pass


def menu():
    print("=================================== Hello to ACRONYM WORLD ===================================")
    print("\nWhat format of ACRONYM do you wish ?")
    print("We have the following Types under our banner :")
    print("\nSuppose the input is New York City")
    print("Press 1 for output : NYC")
    print("Press 2 for output : N.Y.C.")
    print("Press 3 for output : N.Y.C")
    print("\nPlease let us know what format you wish for....")
    choice = int(input())
    return choice


def fn_user_input():
    user_input = input("Enter Your Phrase : ")
    if user_input == "":
        print("Please enter a string and try again ...........")
        fn_user_input()
    return user_input


def main():
    choice = menu()
    user_input = fn_user_input()

    if choice == 1:
        general_acronym(user_input)
    elif choice ==2:
        full_initial(user_input)
    elif choice ==3:
        sp_acronym(user_input)


if __name__ == "__main__":
    main()
