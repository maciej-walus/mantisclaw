from phone_number_information import phone_number_information
def mantisclaw():
    print("\n (  `                    )           (    (                \n )\))(      )         ( /( (         )\   )\    )  (  (    \n((_)()\  ( /(   (     )\()))\  (   (((_) ((_)( /(  )\))(   \n(_()((_) )(_))  )\ ) (_))/((_) )\  )\___  _  )(_))((_)()\  \n|  \/  |((_)_  _(_/( | |_  (_)((_)((/ __|| |((_)_ _(()((_) \n| |\/| |/ _` || ' \))|  _| | |(_-< | (__ | |/ _` |\ V  V / \n|_|  |_|\__,_||_||_|  \__| |_|/__/  \___||_|\__,_| \_/\_/\n")
    print("Welcome to MantisClaw. Select desired function:\n 1. Phone number OSINT\n")
    function = int(input())
    match function:
        case 1:
            print ("\nPhone number OSINT selected.")
            shutdown = False
            pni = phone_number_information()
            while not shutdown:
                print("\nSelect desired functionality:\n 1. Inserting target phone number.\n 2. Print all the phone numbers in the table. \n 3. Print information about phone number(s). \n 4. Shutdown\n")
                osint = int(input())
                match osint:
                    case 1:
                        print("\nInsert the phone number including the country code")
                        phone_number = str(input())
                        pni.save_phone_number(phone_number)

                    case 2:
                        if len(pni.stored_phone_numbers) != 0:
                            print("\nPhone numbers inserted into the table:")
                            for _ in range(len(pni.stored_phone_numbers)):
                                print(pni.stored_phone_numbers[_])
                        else:
                            print("\nNo phone numbers inserted into the table.")

                    case 3:
                        if len(pni.stored_phone_numbers) == 0:
                            print("\nNo phone numbers inserted into the table.")
                        else:
                            print("\nProceed with all phone numbers inserted into the table? \n1. Yes \n2. No, let me pick a specific number")
                            selection = int(input())
                            match selection:
                                case 1:
                                    for _ in range(len(pni.stored_phone_numbers)):
                                        pni.information(pni.stored_phone_numbers[_])

                                case 2:
                                    print("Insert the index of desired phone number:")
                                    index = int(input())
                                    try:
                                        pni.information(pni.stored_phone_numbers[index])
                                    except:
                                        print("Invalid index.")
                                case other:
                                    print("Select a valid option.")

                    case 4:
                        shutdown = True
                        print("\nInto the darkness I descend...")

                    case other:
                        print("Select a valid option.")

        case other:
            print("Select a valid option.")


if __name__ == '__main__':
    mantisclaw()
