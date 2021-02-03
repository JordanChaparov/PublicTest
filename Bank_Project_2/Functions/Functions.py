import pandas as pd
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
from venv.Bank_Project_2.Classes.User_Classes import *
from venv.Bank_Project_2.Classes.Client_Classes import *
from venv.Bank_Project_2.Classes.Accounts_Classes import *


def write_files():
    """
    Initializing the data in csv files, if they don't already exist.
    """

    users_dict = {"First_Name": ["da4ko", "ki4ka", "inokentii", "gustavo", "ronaldo", "batman", "ash", "natsu",
                                 "alphonse", "light", "eren", "roronoa", "mikasa", "dimitri4ka", "kenpachi",
                                 "winry", "kondio", "lucy", "jesus", "riza", "nico", "erza", "touka", "ty",
                                 "mira", "vincent", "rin", "rize"],
                  "Last_Name": ["petrov", "paunova", "nqma", "mehikano", "toolong", "wayne", "ketchum", "dragneel",
                                "elric", "yagami", "yeager", "zoro", "ackerman", "karagiozova", "zaraki", "Rockbell",
                                "djingibi", "heartfilia", "christ", "hawkeye", "robin", "scarlet", "kirishima", "lee",
                                "armstrong", "valantine", "nohara", "kamishiro"],
                  "User_Address": ["4794 drainer avenue", "2173 peck court", "3530 grove avenue", "346 young road",
                                   "1844 stiles street", "2470 clay street", "4583 chatham way", "2676 angus road",
                                   "4180 romano street", "2684 pretty view lane", "2005 high meadow lane",
                                   "2222 charles street", "414 southern avenue", "1247 fort street", "120 lena lane",
                                   "497 maple court", "4507 raver croft drive", "4356 patton lane", "2607 scenic way",
                                   "4682 sunny day drive", "3492 lawman avenue", "705 morgan street", "305 joes road",
                                   "2382 benedum drive", "1291 simpson avenue", "2686 duncan avenue",
                                   "1261  everette alley", "1099 bastin drive"],
                  "User_Email": ["da4kodabest@abv.bg", "nz@abv.bg", "pope@abv.bg", "hispania@abv.mxc",
                                 "zlatnotokopito@abv.bg", "batpost@abv.bg", "pokechamp@abv.bg", "drake@abv.bg",
                                 "FMalchemist@abv.bg", "kira@abv.bg", "titanking@abv.bg", "swordmaster@abv.bg",
                                 "titanslayer@abv.bg", "dimi@abv.bg", "shinigami@abv.bg", "mech@abv.bg", "doko@abv.bg",
                                 "luci@abv.bg", "sonofgod@abv.bg", "hawkeye@abv.bg", "devil@abv.bg", "scarlet@abv.bg",
                                 "tokyoghoul@abv.bg", "tylee@abv.bg", "armstrong@abv.bg", "vince@abv.bg", "rin@abv.bg",
                                 "rize@abv.bg"],
                  "User_Phone": ["0899135186", "0899531168", "0899168531", "0899057385", "0899077355", "0899070353",
                                 "0899097531", "0899135790", "0899246801", "0899102938", "0899938576", "0899850264",
                                 "0899864086", "0899356487", "0899563209", "0899769854", "0899007733", "0899150375",
                                 "7777777777", "0899359175", "0899789245", "0899864108", "0899654198", "0899145790",
                                 "0899540831", "0899671351", "0899764345", "0899158935"],
                  "Password": ["imdabest", "ohnz", "amin", "porfavor", "football", "secret", "pokemaster",
                               "dragonslayer", "metal", "death", "humanity", "yubashiri", "scarf", "kifla", "bankai",
                               "mechanic", "doko", "summoner", "god", "adjutant", "poneglyph", "armor", "ghoul",
                               "bender", "generations", "stigma", "dream", "cannibal"],
                  "Pass_Check": ["imdabest", "ohnz", "amin", "porfavor", "football", "secret", "pokemaster",
                                 "dragonslayer", "metal", "death", "humanity", "yubashiri", "scarf", "kifla", "bankai",
                                 "mechanic", "doko", "summoner", "god", "adjutant", "poneglyph", "armor", "ghoul",
                                 "bender", "generations", "stigma", "dream", "cannibal"],
                  "User_Id": ["2301269978", "3202167280", "4001269978", "8609073589", "6012251234", "7211064437",
                              "1104305547", "9010183208", "9805158965", "0507066852", "2506043698", "5807023246",
                              "6101235817", "5808317746", "1608317943", "4102097449", "5207228283", "7502059367",
                              "0407203214", "3412196305", "4302121134", "2507222522", "8903252123", "3603034312",
                              "3203182237", "8303064649", "3805257718", "7801261176"],
                  "User_Access": ["Admin", "Employee", "User", "User", "User", "Employee", "User", "User", "User",
                                  "User", "User", "User", "User", "User", "User", "User", "User", "User", "Admin",
                                  "User", "User", "User", "User", "User", "User", "User", "Employee", "User"],
                  "User_Type": ["individual", "individual", "individual", "individual", "individual", "individual",
                                "individual", "individual", "individual", "individual", "individual", "individual",
                                "individual", "individual", "individual", "individual", "individual", "individual",
                                "individual", "individual", "individual", "individual", "individual", "individual",
                                "individual", "individual", "individual", "individual"]}

    firms_dict = {"Firm_Name": ["bionism", "spinuke", "histics", "neowire", "digies", "nerdalytics", "exowire",
                                "microvox", "telecoil", "digitech", "cryptech", "dynatech", "audionics", "qunatumcore"],
                  "Firm_Address": ["4794 drainer avenue", "2173 peck court", "3530 grove avenue", "346 young road",
                                   "1844 stiles street", "2470 clay street", "4583 chatham way", "801  hope street",
                                   "4934  fittro street", "4418  white oak drive", "1303  fairfield road",
                                   "2669  sardis sta", "2897  armbrester drive", "751  mcwhorter road"],
                  "Manager": ["curtis w schwenk", "richard e mobley", "jesse s ruiz", "mona j wheless",
                              "waltraud a morrison", "susan m brown", "lonnie m boyd", "esperanza h max",
                              "william a battle", "bradford j lovett", "john n daly", "barbara c clegg",
                              "justine d evans", "julio c johnson"],
                  "Password": ["curtis", "richard", "jesse", "mona", "waltraud", "susan", "lonnie", "esperanza",
                               "william", "bradford", "john", "barbara", "justine", "julio"],
                  "Pass_Check": ["curtis", "richard", "jesse", "mona", "waltraud", "susan", "lonnie", "esperanza",
                                 "william", "bradford", "john", "barbara", "justine", "julio"],
                  "Firm_Id": ["337513922", "346131592", "266769273", "530668176", "887911665", "194737179",
                              "108760343", "367132817", "350561484", "367579080", "195568949", "505561414",
                              "990563697", "218460977"],
                  "User_Type": ["firm", "firm", "firm", "firm", "firm", "firm", "firm", "firm", "firm", "firm", "firm",
                                "firm", "firm", "firm"],
                  "Client_Access": ["User", "User", "User", "User", "User", "User", "User", "User", "Employee", "User",
                                    "User", "User", "User", "User"]}

    acc_dict = {"Client": ["da4ko", "ki4ka", "inokentii", "gustavo", "bionism", "spinuke", "neowire", "nerdalytics",
                           "qunatumcore", "telecoil", "cryptech", "kondio", "kondio", "kondio", "kondio"],
                "Balance": [7000, 5000, 10000, 3100, 15000, 12000, 7500, 9250, 6300, 8700, 2900, 900, 5754, 7000, 5000],
                "Interest": [2, 3, 5, 3, 2, 3, 5, 3, 4, 3, 4, 5, 2, 3, 5],
                "Account_Type": ["deposit", "deposit", "credit", "mortgage", "credit", "deposit", "deposit", "credit",
                                 "mortgage", "deposit", "credit", "deposit", "credit", "mortgage", "deposit"]}

    if not os.path.exists("../Bank_Project_2/Accounts.csv"):                  # checks if the file already exists
        acc_data = pd.DataFrame(data=acc_dict)                                # if not it writes(initialize) it
        acc_data.to_csv("../Bank_Project_2/Accounts.csv", index=False)        # writing it to csv with no indexes
    if not os.path.exists("../Bank_Project_2/Users.csv"):
        user_data = pd.DataFrame(data=users_dict)
        user_data.to_csv("../Bank_Project_2/Users.csv", index=False)
    if not os.path.exists("../Bank_Project_2/Firms.csv"):
        firms_data = pd.DataFrame(data=firms_dict)
        firms_data.to_csv("../Bank_Project_2/Firms.csv", index=False)


def register_user():
    """
    Handling user registration. Asking the user to register an individual or a firm. After filling the information an
    object of class (depending on the choice) is made which is later registered and written in the user or the firms
    database (again depending on the user's choice).
    :return: object of class Individual or class Firm, which is registered and written on csv file.
    """
    subject = input("Welcome to Da4ko's bank. Do you want to register individual or firm?").strip().lower()

    if subject == "individual":
        print("\nPlease, type your information to register an account.")
        first_name = input("Enter your name: ").strip().lower()
        last_name = input("Enter your last name: ").strip().lower()
        address = input("Enter your address: ").strip().title()
        email = input("Enter your email here: ").strip()
        phone = input("Enter your phone: ").strip()
        password = input("Enter your password here: ").strip()
        pass_check = input("Enter your password again: ").strip()
        personal_id = input("Enter your personal id: ").strip()

        # below we instance an object of the User class
        person = User(first_name, last_name, address, email, phone, password, pass_check, personal_id)

        # below we get the user's data from class object and save it to a list for later use
        user_list = [person.get_first_name(), person.get_last_name(), person.get_address(), person.get_email(),
                     person.get_phone(), person.get_password(), person.get_pass_check(), person.get_id(),
                     person.get_access(), person.get_client_type()]

        with open("../Bank_Project_2/Users.csv", mode="a", newline="") as f:    # opening file in add mode
            writer = csv.writer(f, delimiter=",")
            with open("../Bank_Project_2/Users.csv", mode="r") as g:
                reader = csv.reader(g, delimiter=",")
                if person.get_password() != person.get_pass_check():
                    print("Password doesn't match the check, please try again.")
                    return
                else:
                    for row in reader:
                        if person.get_email() == row[3]:
                            print("User with such email already exists.")
                            return
                writer.writerow(user_list)
                print("You are now registered.")
    elif subject == "firm":
        print("\nPlease, type your information to register an account.")
        firm_name = input("Enter the firm's name: ").lower().strip()
        firm_address = input("Enter the firm's address: ").lower().strip()
        firm_manager = input("Enter the firm's manager: ").lower().strip()
        firm_password = input("Enter a password: ").lower().strip()
        firm_pass_check = input("Repeat the password: ").lower().strip()
        firm_id = input("Enter the firm's id: ").lower().strip()

        firm = Firm(firm_name, firm_address, firm_manager, firm_password, firm_pass_check, firm_id)

        firm_list = [firm.get_client_name(), firm.get_client_address(), firm.get_manager(), firm.get_client_password(),
                     firm.get_client_pass_check(), firm.get_client_id(), firm.get_client_type(),
                     firm.get_client_access()]

        with open("../Bank_Project_2/Firms.csv", mode="a", newline="") as f:    # opening file in add mode
            writer = csv.writer(f, delimiter=",")
            with open("../Bank_Project_2/Firms.csv", mode="r") as g:
                reader = csv.reader(g, delimiter=",")
                if firm.get_client_password() != firm.get_client_pass_check():
                    print("Password doesn't match the check, please try again.")
                    return
                else:
                    for row in reader:
                        if firm.get_client_id() == row[5]:
                            print("Firm with such id already exists.")
                            return
                writer.writerow(firm_list)
                print("Your firm is now registered.")
    else:
        print("You can't register ", subject, " please choose individual or firm!!!")
        return


def login_user():
    """
    Handling user/firm login. Depending on the choice:
    Ask for user email and password, checking if the data is correct and then log in (if not logged in).
    Or ask for firm id and password, checking if the data is correct and then log in (if not logged in).
    :return: Access if user/firm is found otherwise empty string.
    """
    login = input("Hello, how would you like to be logged in as user or firm?").strip().lower()

    if login == "user":
        print("\nTo login, please enter your email and password: ")
        email = input("Enter your email here: ").strip().lower()
        password = input("Enter your password here: ").strip().lower()
        with open("../Bank_Project_2/Users.csv", mode="r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if row[3] == email and row[5] == password:                       # if name and pass check we log in user
                    print(row[8])
                    print("\nWelcome. You are now logged in as: " + row[0] + ".")
                    return row[8]                                                # we return the user's access
        print("Incorrect username/password or you are not logged in.")
        return ""
    if login == "firm":
        print("\nTo login, please enter your id and password: ")
        firm_id = input("Enter your firm's id: ")
        firm_pass = input("Enter your password: ")
        with open("../Bank_Project_2/Firms.csv", mode="r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if firm_id == row[5] and firm_pass == row[3]:
                    print(row[7])
                    print("\n Welcome. You are now logged in as " + row[0] + ".")
                    return row[7]
        print("Incorrect firm id/password or you are not logged in.")
        return ""
    else:
        print("You can't log in as ", login, ",please choose from user or firm!!!")


def open_account():
    """
    Opening new accounts depending on the choice, they could be deposit, credit or mortgage.
    :return: account_list with new data, which is written in Account.csv file.
    """

    account = input("What type of account do you want to open - deposit/credit/mortgage?").lower().strip()

    if account == "deposit":
        acc_name = input("Enter your name: ").strip().lower()
        acc_balance = int(input("Enter the balance: "))
        acc_interest = int(input("Enter the interest: "))

        dep = Deposit(acc_name, acc_balance, acc_interest)                         # instancing Deposit subclass object
        account_list = [dep.get_client(), dep.get_balance(), dep.get_interest(), dep.get_acc_type()]

        with open("../Bank_Project_2/Accounts.csv", mode="a", newline="") as f:    # opening file in add mode
            writer = csv.writer(f, delimiter=",")
            writer.writerow(account_list)                                          # adding new data to the file
            print("Your account has been created.")

    elif account == "credit":
        acc_name = input("Enter your name: ").strip().lower()
        acc_balance = int(input("Enter the balance: "))
        acc_interest = int(input("Enter the interest: "))

        cr = Credit(acc_name, acc_balance, acc_interest)                         # instancing Credit subclass object
        account_list = [cr.get_client(), cr.get_balance(), cr.get_interest(), cr.get_acc_type()]

        with open("../Bank_Project_2/Accounts.csv", mode="a", newline="") as f:  # opening file in add mode
            writer = csv.writer(f, delimiter=",")
            writer.writerow(account_list)                                        # adding new data to the file
            print("Your account has been created.")

    elif account == "mortgage":
        acc_name = input("Enter your name: ").strip().lower()
        acc_balance = int(input("Enter the balance: "))
        acc_interest = int(input("Enter the interest: "))

        mort = Credit(acc_name, acc_balance, acc_interest)                       # instancing Mortgage subclass object
        account_list = [mort.get_client(), mort.get_balance(), mort.get_interest(), mort.get_acc_type()]

        with open("../Bank_Project_2/Accounts.csv", mode="a", newline="") as f:  # opening file in add mode
            writer = csv.writer(f, delimiter=",")
            writer.writerow(account_list)                                        # adding new data to the file
            print("Your account has been created.")
    else:
        print("You can't create ", account, ", please choose from deposit, credit or mortgage!!!")


def show_account():
    """
    Asking if the user is user or firm. Depending on the choice:
    Asking for user's email to link him/her from the Users database. If the user has "user" access, the function
    prints only his bank account(s), otherwise the whole database is printed.
    Or asking for firm's id to link it from the Firms database. If the firm has "user" access, the function
    prints only its bank account(s), otherwise the whole database is printed.
    """

    acc = input("Are you user or firm?").lower().strip()
    if acc == "user":
        email = input("Please enter your email: ").strip().lower()
        with open("../Bank_Project_2/Users.csv", mode="r") as j:
            reader1 = csv.reader(j, delimiter=",")
            for row1 in reader1:
                if row1[3] == email:                                              # if email checks we get user's name
                    name = row1[0]
                    if row1[8] == "User":                                         # depending on the access we show data
                        with open("../Bank_Project_2/Accounts.csv", mode="r") as f:
                            reader = csv.reader(f, delimiter=",")
                            print("\nThese are all the accounts:")
                            for row in reader:
                                if name == row[0]:                                   # if account/s with such name exist
                                    print(row[0], row[1] + "$", row[2] + "%", row[3])    # show his/her the data
                    else:
                        with open("../Bank_Project_2/Accounts.csv", mode="r") as f:   # if the user is bank employee or
                            reader = csv.reader(f, delimiter=",")                     # admin we show all the accounts
                            print("\nThese are all the accounts:")
                            for row in reader:
                                print(row[0], row[1] + "$", row[2] + "%", row[3])
    elif acc == "firm":
        firm_id = input("Please enter your firm id: ").strip().lower()
        with open("../Bank_Project_2/Firms.csv", mode="r") as j:
            reader1 = csv.reader(j, delimiter=",")
            for row1 in reader1:
                if row1[5] == firm_id:                                              # if id checks we get firm's name
                    name = row1[0]
                    if row1[7] == "User":                                         # depending on the access we show data
                        with open("../Bank_Project_2/Accounts.csv", mode="r") as f:
                            reader = csv.reader(f, delimiter=",")
                            print("\nThese are all the accounts:")
                            for row in reader:
                                if name == row[0]:                                # if account(s) with such name exist
                                    print(row[0], row[1] + "$", row[2] + "%", row[3])     # we show his/her data
                    else:
                        with open("../Bank_Project_2/Accounts.csv", mode="r") as f:   # if the user is bank employee or
                            reader = csv.reader(f, delimiter=",")                     # admin we show all the accounts
                            print("\nThese are all the accounts:")
                            for row in reader:
                                print(row[0], row[1] + "$", row[2] + "%", row[3])
    else:
        print("You are not ", acc, ", please choose from user or firm!!!")          # don't mess with the system


def menu():
    """
    Showing the user all the options in the program according to his access. Executing various function on user's call.
    """
    online = True
    logged_in = ""

    while online:
        if logged_in == "User":                            # depending on the access we show different menu for the user
            print("\nLogout\nOpen Account\nShow Account\nCalculate Interest\nDeposit\nWithdraw\nQuit")
        elif logged_in == "Employee":
            print("\nLogout\nOpen Account\nShow Account\nCalculate Interest\nDeposit\nWithdraw\nQuit")
        elif logged_in == "Admin":
            print("\nLogout\nRemove Record\nManage Users\nOpen Account\nShow Account\nCalculate Interest\nDeposit"
                  "\nWithdraw\nShow Chart\nQuit")
        else:
            print("\nRegister\nLogin\nQuit")

        choice = input("\nWhat would you like to do? ").strip().title()     # depending on the choice and if the user is
        if choice == "Register" and logged_in == "":                        # logged we call various functions
            register_user()
        elif choice == "Login" and not logged_in:
            logged_in = login_user()
        elif choice == "Open Account" and logged_in:
            open_account()
        elif choice == "Show Account" and logged_in:
            show_account()
        elif choice == "Calculate Interest" and logged_in:
            calc_interest()
        elif choice == "Deposit" and logged_in:
            deposit()
        elif choice == "Withdraw" and logged_in:
            withdraw()
        elif choice == "Logout" and logged_in:
            logged_in = ""
            print("You are now logged out.")
        elif choice == "Remove Record" and logged_in == "Admin":
            remove_record()
        elif choice == "Manage Users" and logged_in == "Admin":
            manage_users()
        elif choice == "Show Chart" and logged_in == "Admin":
            show_chart()
        elif choice == "Quit":
            online = False
            print("Thanks for using this program!")
        else:
            print("Sorry you can't " + str(choice) + ". Please, choose an option from the menu.")


def calc_interest():
    """
    Asking if the user is user or firm, depending on the choice:
    Asking for user's email/firm id to link him to the Users/Firms database and then calculating the interest, which is
    calculated as follows: balance * interest / 100
    pick - int of user input, if more than one account is available to pick from the dictionary
    int(value[1]) - int from user's balance recorded in the dictionary
    int(value[2]) - int from user's interest recorded in the dictionary
    n - user input for how many months to calculate the interest
    Depending on the user type (user/firm) and account type (deposit/credit/mortgage) there are different type of
    discount.
    :return: int from calc variable
    """
    calc_acc = input("Are you user or firm?").strip().lower()              # asking if the user is user or firm
    accs = {}

    if calc_acc == "user":
        email = input("Please enter your email: ").strip().lower()
        with open("../Bank_Project_2/Users.csv", mode="r") as j:
            reader1 = csv.reader(j, delimiter=",")
            for row1 in reader1:
                if row1[3] == email:                                       # if email checks we get the user's name
                    name = row1[0]

        with open("../Bank_Project_2/Accounts.csv", mode="r") as g:
            reader = csv.reader(g, delimiter=",")

            i = 0                                                          # setting index value to 0
            for row in reader:
                if row[0] == name:                                         # if name checks we add to the dictionary
                    i += 1                                                 # and increasing index with 1
                    accs[i] = row

            for key, value in accs.items():
                print(key, value, end="\n")                                # printing all the choices(accounts)

            pick = int(input("Which account do you want to check?"))       # we pick the exact account to check

            for key, value in accs.items():
                if pick == key:                                            # matching the pick with the right key
                    print(value)
                    if value[3] == "deposit":                              # check if the account is deposit
                        print("The deposit has no interest if your balance is positive and under 1000$.")
                        if int(value[1]) < 1000:                           # setting the condition
                            value[2] = 0
                        else:                                              # if its not met we do some math... *cry*
                            n = int(input("For how many months you want to calculate the interest?"))     # guess
                            month = (int(value[1]) * int(value[2])) / 100                  # float type is annoying
                            print("The interest for 1 month is->", int(month), "$.")       # printing cuz i cant do math
                            calc = int(month) * n
                            print("The interest for {} months is {}$".format(n, calc))     # and here we multiply by n
                    elif value[3] == "credit":                                             # new type new rules
                        print("The credit has no interest for the first 3 months.")        # giving the good news
                        n = int(input("For how many months you want to calculate the interest?"))         # same again
                        month = (int(value[1]) * int(value[2])) / 100                      # the magic happens here
                        print("The interest for 1 month is:", int(month), "$")             # get your calculators out
                        print("Removing the interest for the first 3 months.")  # lazy way...
                        calc = (int(month) * n) - (int(month) * 3)
                        if calc < 0:                                                        # being more lazy...
                            print("The interest for {} months is 0$.".format(n))            # No math, no cry! - Da4ko
                        else:
                            print("The interest for {} months is {}$.".format(n, calc))     # giving the bad news
                    elif value[3] == "mortgage":                                            # tired... need sleep
                        print("The mortgage has no interest for the first 6 months.")
                        n = int(input("For how many months you want to calculate the interest?"))
                        month = (int(value[1]) * int(value[2])) / 100
                        print("The interest for 1 month is:", int(month), "$")
                        print("Removing the interest for the first 6 months.")
                        calc = (int(month) * n) - (int(month) * 6)
                        if calc < 0:
                            print("The interest for {} months is 0$.".format(n))
                        else:
                            print("The interest for {} months is {}$.".format(n, calc))

    elif calc_acc == "firm":                                                    # we do the above with new conditions
        calc_firm_id = input("Please enter your firm id: ").strip().lower()
        with open("../Bank_Project_2/Firms.csv", mode="r") as s:
            reader1 = csv.reader(s, delimiter=",")
            for row1 in reader1:
                if row1[5] == calc_firm_id:                                # if id checks we get the firm's name
                    name = row1[0]

        with open("../Bank_Project_2/Accounts.csv", mode="r") as g:
            reader = csv.reader(g, delimiter=",")

            i = 0                                                          # setting index value to 0
            for row in reader:
                if row[0] == name:                                         # if name checks we add to the dictionary
                    i += 1                                                 # and increasing index with 1
                    accs[i] = row

            for key, value in accs.items():
                print(key, value, end="\n")                                # printing all the choices(accounts)

            pick = int(input("Which account do you want to check?"))       # we pick the exact account to check

            for key, value in accs.items():
                if pick == key:
                    print(value)
                    if value[3] == "deposit":
                        print("The deposit has no interest if your balance is positive and under 1000$.")
                        if int(value[1]) < 1000:
                            value[2] = 0
                        else:
                            n = int(input("For how many months you want to calculate the interest?"))
                            month = (int(value[1]) * int(value[2])) / 100
                            print("The interest for 1 month is->", int(month), "$.")
                            calc = int(month) * n
                            print("The interest for {} months is {}$".format(n, calc))
                    elif value[3] == "credit":
                        print("The credit has no interest for the first 2 months.")
                        n = int(input("For how many months you want to calculate the interest?"))
                        month = (int(value[1]) * int(value[2])) / 100
                        print("The interest for 1 month is:", int(month), "$")
                        print("Removing the interest for the first 2 months.")
                        calc = (int(month) * n) - (int(month) * 2)
                        if calc < 0:
                            print("The interest for {} months is 0$.".format(n))
                        else:
                            print("The interest for {} months is {}$.".format(n, calc))
                    elif value[3] == "mortgage":
                        print("The mortgage has half of interest for the first 12 months.")
                        n = int(input("For how many months you want to calculate the interest?"))
                        month = (int(value[1]) * int(value[2])) / 100
                        half = month/2
                        print("The interest for 1 month is:", int(month), "$")
                        print("Reducing the interest for the first 12 months by half.")
                        if n < 12:
                            calc = int(half) * n
                            print("The interest for {} months is {}$.".format(n, calc))
                        else:
                            calc = (int(month) * n) - (int(half) * 12)                      # or int(month) * 6
                            print("The interest for {} months is {}$.".format(n, calc))
    else:
        print("Your are not ", calc_acc, ", please choose from user or firm!!!")


def deposit():
    """
    Asking if the user is user or firm, depending on the choice:
    Asking for user's email/firm's id to link it to Users/Firms database and then adding money to his/her account.
    The user can pick to which account he/she wants to deposit.
    :return: accs dictionary with new balance value, which is later written in Accounts.csv file.
    """
    rows = []
    accs = {}
    entry = input("Are you user or firm?").strip().lower()

    if entry == "user":
        email = input("Please enter your email: ").strip().lower()
        with open("../Bank_Project_2/Users.csv", mode="r") as j:
            reader1 = csv.reader(j, delimiter=",")
            for row1 in reader1:
                if row1[3] == email:                                           # if email checks we get the user's name
                    name = row1[0]
    elif entry == "firm":
        dep_firm_id = input("Please enter your firm id: ").strip().lower()
        with open("../Bank_Project_2/Firms.csv", mode="r") as s:
            reader1 = csv.reader(s, delimiter=",")
            for row1 in reader1:
                if row1[5] == dep_firm_id:                                      # if id checks we get the firm's name
                    name = row1[0]
    else:
        print("You are not ", entry, ", please choose from user or firm!!!")

    with open("../Bank_Project_2/Accounts.csv", mode="r") as g:
        reader = csv.reader(g, delimiter=",")

        i = 0                                                              # setting index value to 0
        for row in reader:
            rows.append(row)                                               # appending all rows in the file to rows list
            if row[0] == name:                                             # if name checks we add to the dictionary
                i += 1                                                     # and increasing index with 1
                accs[i] = row
                rows.remove(row)

        for key, value in accs.items():
            print(key, value, end="\n")                                    # printing all the choices(accounts)

        pick = int(input("Which account do you want to deposit to?"))      # we pick the exact account to deposit

        for key, value in accs.items():
            if pick == key:                                                # if pick match the dict key we calculate
                deposit_value = int(input("How much money do you want to deposit?"))
                added = int(value[1]) + deposit_value
                print("You had {}. You deposited {}, and now you have {}.".format(value[1], deposit_value, added))
                value[1] = int(added)

    with open("../Bank_Project_2/Accounts.csv", mode="w", newline="") as h:   # writing the new record to the csv file
        writer = csv.writer(h, delimiter=",")
        writer.writerows(rows)                                                # new_record always last since we want
        for v in accs.values():                                               # to keep the header on top
            writer.writerow(v)


def withdraw():
    """
    Asking if the user is user or firm, depending on the choice:
    Asking for user's email/firm's id to link it to Users/Firms database and then taking money from his/her account.
    If the amount of money the user/firm wants to withdraw is higher than the balance, error message is displayed and
    he/she is returned to the menu. The user can pick from which account he/she wants to withdraw.
    :return: accs dictionary with new balance value, which is later written in Accounts.csv file.
    """
    rows = []
    accs = {}

    entry2 = input("Are you user or firm?").strip().lower()

    if entry2 == "user":
        email = input("Please enter your email: ").strip().lower()
        with open("../Bank_Project_2/Users.csv", mode="r") as j:
            reader1 = csv.reader(j, delimiter=",")
            for row1 in reader1:
                if row1[3] == email:                                       # if email checks we get the user's name
                    name = row1[0]
    elif entry2 == "firm":
        w_firm_id = input("Please enter your firm id: ").strip().lower()
        with open("../Bank_Project_2/Firms.csv", mode="r") as s:
            reader1 = csv.reader(s, delimiter=",")
            for row1 in reader1:
                if row1[5] == w_firm_id:                                   # if id checks we get the firm's name
                    name = row1[0]
    else:
        print("You are not ", entry2, ", please choose from user or firm!!!")

    with open("../Bank_Project_2/Accounts.csv", mode="r") as g:
        reader = csv.reader(g, delimiter=",")

        i = 0                                                              # setting index value to 0
        for row in reader:
            rows.append(row)                                               # appending all rows in the file to rows list
            if row[0] == name:                                             # if name checks we add to the dictionary
                i += 1                                                     # and increasing index with 1
                accs[i] = row
                rows.remove(row)

    for key, value in accs.items():
        print(key, value, end="\n")                                            # printing all the choices(accounts)

    pick = int(input("Which account do you want to withdraw from?"))           # pick the exact account to withdraw

    for key, value in accs.items():
        if pick == key:                                                        # if pick match the dict key we calculate
            if value[3] == "deposit":
                withdraw_value = int(input("How much money do you want to withdraw?"))
                if int(value[1]) < withdraw_value:
                    print("You don't have sufficient funds!")
                    return
                else:
                    withdrawal = int(value[1]) - withdraw_value
                    print("You had {}. You deposited {}, and now you have {}.".format(value[1], withdraw_value,
                                                                                      withdrawal))
                    value[1] = int(withdrawal)

                with open("../Bank_Project_2/Accounts.csv", mode="w", newline="") as h:     # writing the new record
                    writer = csv.writer(h, delimiter=",")
                    writer.writerows(rows)                                    # new_record always last since we want
                    for v in accs.values():                                   # to keep the header on top
                        writer.writerow(v)
            else:
                print("Your account type is not deposit, so you can't withdraw money from it.")
                return


def manage_users():
    """
    Asking for user's email or firm's id to link them from the database. After that asking the admin which part of the
    data he/she wants to change. Then asking to input the new data, which replaces the old one and its written in
    the database csv file.
    :return: new_record which is altered data for any user/firm. The data is written on the csv file.
    """
    account = input("What type of account do you want to manage, individual or firm?").lower().strip()

    if account == "individual":
        rows = []
        new_record = []
        with open("../Bank_Project_2/Users.csv", mode="r") as j:
            reader = csv.reader(j, delimiter=",")
            email = input("Type the email of the user you want to change: ").strip().lower()
            for row in reader:
                rows.append(row)                  # appending all rows from the file in the rows list
                if email == row[3]:
                    new_record.append(row[0])     # if email matches the data appending all data from this row in
                    new_record.append(row[1])     # new_record list
                    new_record.append(row[2])
                    new_record.append(row[3])
                    new_record.append(row[4])
                    new_record.append(row[5])
                    new_record.append(row[6])
                    new_record.append(row[7])
                    new_record.append(row[8])
                    rows.remove(row)              # removing the row on which the email matched since it will be changed

            i = 0                                 # printing the new record list so the admin sees the data
            for item in new_record:
                print(i, item)
                i += 1

            n = int(input("\nWhich part of the user data do you want ot change?"))  # picking the data to be changed
            i = -1                                                                  # consequence of stupid mistake
            for item in new_record:
                i += 1                                                             # the stupid mistake (should be last)
                if n == i:                                                         # check the input with data number
                    print("The data of the user you want to change is: ", item)
                    change = input("Enter the new data: ").strip()                # no .lower() since file format is bad
                    new_record[i] = change
            print("User's data after the change: \n", new_record)

            with open("../Bank_Project_2/Users.csv", mode="w", newline="") as f:  # writing the new data on Users.csv
                writer = csv.writer(f, delimiter=",")
                writer.writerows(rows)
                writer.writerow(new_record)

    elif account == "firm":
        rows = []                                 # wonder why i don't do it on the top of the function... and twice
        new_record = []
        with open("../Bank_Project_2/Firms.csv", mode="r") as j:
            reader = csv.reader(j, delimiter=",")
            firm_id = input("Enter the firm's id: ").lower().strip()
            for row in reader:
                rows.append(row)
                if firm_id == row[5]:
                    new_record.append(row[0])     # if the id matches the data appending all data from this row in
                    new_record.append(row[1])     # new_record list
                    new_record.append(row[2])
                    new_record.append(row[3])
                    new_record.append(row[4])
                    new_record.append(row[5])
                    new_record.append(row[6])
                    new_record.append(row[7])
                    rows.remove(row)              # removing the row on which the email matched since it will be changed

            i = 0                                 # printing the new record list so the admin sees the data
            for item in new_record:
                print(i, item)
                i += 1

            n = int(input("\nWhich part of the firm data do you want ot change?"))  # picking the data to be changed
            i = -1                                                                  # consequence of stupid mistake
            for item in new_record:
                i += 1                                                         # the stupid mistake (should be last)
                if n == i:                                                     # check the input with data number
                    print("The data of the firm you want to change is: ", item)
                    change = input("Enter the new data: ").strip()            # no .lower() since file format is bad
                    new_record[i] = change
            print("Firm's data after the change: \n", new_record)

            with open("../Bank_Project_2/Firms.csv", mode="w", newline="") as f:  # writing the new data on Firms
                writer = csv.writer(f, delimiter=",")
                writer.writerows(rows)
                writer.writerow(new_record)
    else:
        print("You can't change ", account, " type of account. Please choose from individual or firm.")


def remove_record():
    """
    Asking the admin from which file he wants to remove record. If its user we ask for the email, if firm for the id.
    From the accounts file we use dictionary and use its keys to remove the record we want.
    :return: rows list which contains all the records in the file except for the deleted one.
    """
    record = input("What do you want to remove User, Firm or Account?").strip().capitalize()
    rows = []
    accs = {}
    if record == "User":
        with open("../Bank_Project_2/Users.csv", mode="r") as j:
            reader = csv.reader(j, delimiter=",")
            email = input("Type the email of the user you want to remove: ").strip().lower()
            for row in reader:
                rows.append(row)                                    # appending all rows from the file in the rows list
                if email == row[3]:
                    print("Removing record:\n", row)                # visualizing the record for self confirmation
                    rows.remove(row)                                # removing the row on which the email matched
        with open("../Bank_Project_2/Users.csv", mode="w", newline="") as f:         # writing the new data in Users.csv
            writer = csv.writer(f, delimiter=",")
            writer.writerows(rows)
        print("User removed.")
    elif record == "Firm":
        with open("../Bank_Project_2/Firms.csv", mode="r") as j:
            reader = csv.reader(j, delimiter=",")
            firm_id = input("Enter the firm's id of the firm you want to remove: ").lower().strip()
            for row in reader:
                rows.append(row)                                    # appending all rows from the file in the rows list
                if firm_id == row[5]:
                    print("Removing record:\n", row)                # visualizing the record for self confirmation
                    rows.remove(row)                                # removing the row on which the email matched
        with open("../Bank_Project_2/Firms.csv", mode="w", newline="") as f:         # writing the new data in Firms.csv
            writer = csv.writer(f, delimiter=",")
            writer.writerows(rows)
        print("Firm removed.")
    elif record == "Account":
        with open("../Bank_Project_2/Accounts.csv", mode="r") as g:
            reader = csv.reader(g, delimiter=",")

            i = 0
            for row in reader:
                i += 1
                accs[i] = row                                                    # we use dictionary here for the keys
                rows.append(row)                                                 # and list too cuz we can yay

            for key, value in accs.items():
                print(key, value, end="\n")                                      # printing all the accounts

            pick = int(input("Which account do you want to remove?"))        # we pick the exact account to remove

            for key, value in accs.items():
                if pick == key:                                                  # if pick match the dict key we remove
                    print("Removing record:\n", value)                    # visualizing the record for self confirmation
                    rows.remove(row)

        with open("../Bank_Project_2/Accounts.csv", mode="w", newline="") as f:  # writing the new data in Accounts.csv
            writer = csv.writer(f, delimiter=",")
            writer.writerows(rows)                                            # can write dict values instead... but why
        print("Account removed.")
    else:
        print("Don't be stupid, pick one of the three!")                         # ye don't be stupid


def show_chart():
    """
    Printing the number of accounts by types. Printing the number of users and firms that have made an account.
    Showing pie chart for the client's share in the bank balance. Showing table for the user's balance and type account
    in the bank.
    """
    account_names = []
    user_count = 0
    firm_count = 0
    d = pd.read_csv("../Bank_Project_2/Accounts.csv")
    print()
    print("Number of accounts by type:")
    print(d["Account_Type"].value_counts())

    with open("../Bank_Project_2/Accounts.csv", mode="r") as g:
        reader = csv.reader(g, delimiter=",")
        for row in reader:
            account_names.append(row[0])
    with open("../Bank_Project_2/Firms.csv", mode="r") as g:
        reader1 = csv.reader(g, delimiter=",")
        for row in reader1:
            if row[0] in account_names:
                firm_count += 1
            else:
                user_count += 1
    print("\nNumber of users that have made an account is: ", user_count)
    print("Number of firms that have made an account is: ", firm_count)

    chart1 = pd.read_csv("../Bank_Project_2/Accounts.csv")
    bal, client, text = plt.pie(chart1["Balance"], labels=chart1["Client"], autopct="%.1f")
    plt.title("Client's share in Da4ko's Bank")
    plt.axis("equal")
    plt.show()

    plt.figure(figsize=(24, 12))
    plt.ylim(0, 16000)
    data = [[7000, 5000, 0, 0, 0, 12000, 7500, 0, 0, 8700, 0, 500, 0, 0, 5000],
            [0, 0, 10000, 0, 15000, 0, 0, 9250, 0, 0, 2900, 0, 5754, 0, 0],
            [0, 0, 0, 3100, 0, 0, 0, 0, 6300, 0, 0, 0, 0, 7000, 0]]
    columns = ["da4ko", "ki4ka", "inokentii", "gustavo", "bionism", "spinuke", "neowire", "nerdalytics",
               "qunatumcore", "telecoil", "cryptech", "kondio", "kondio", "kondio", "kondio"]
    rows = ("Deposit", "Credit", "Mortgage")

    colors = plt.cm.BuPu(np.linspace(0.3, 0.6, len(rows)))
    n_rows = len(data)
    index = np.arange(len(columns))
    bar_width = 0.3

    cell_text = []
    print("\n", rows)
    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, color=colors[row])
        y_offset = data[row]
        cell_text.append(y_offset)
        print()
        print(y_offset)

    the_table = plt.table(rowLabels=rows, colLabels=columns, cellText=cell_text, rowColours=colors, loc="bottom")

    plt.subplots_adjust(left=0.2, bottom=0.2)
    plt.ylabel("Balance")
    plt.xticks([])
    plt.title("Da4ko's Bank")
    plt.show()
