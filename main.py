from phone_number_information import phone_number_information
import phonenumbers


def mantisclaw():
    print("\n (  `                    )           (    (                \n )\))(      )         ( /( (         )\   )\    )  (  (    \n((_)()\  ( /(   (     )\()))\  (   (((_) ((_)( /(  )\))(   \n(_()((_) )(_))  )\ ) (_))/((_) )\  )\___  _  )(_))((_)()\  \n|  \/  |((_)_  _(_/( | |_  (_)((_)((/ __|| |((_)_ _(()((_) \n| |\/| |/ _` || ' \))|  _| | |(_-< | (__ | |/ _` |\ V  V / \n|_|  |_|\__,_||_||_|  \__| |_|/__/  \___||_|\__,_| \_/\_/\n")
    print("Welcome to MantisClaw. Select desired function:\n 1. Phone number OSINT\n")
    function = int(input())

    if function == 1:
        print ("\nPhone number OSINT selected.")
        shutdown = False
        pni = phone_number_information()
        phone_function = 0
        info_function = 0

        while shutdown != True:

            print("\nSelect desired functionality:\n 1. Inserting target phone number.\n 2. Print all the phone numbers in the table. \n 3. Print information about phone number(s). \n 4. Shutdown\n")
            phone_function = int(input())

            if phone_function == 1:
                print("\nInsert the phone number including the country code")
                phone_number = str(input())
                pni.save_phone_number(phone_number)
                phone_function = -1

            if phone_function == 2:
                if len(pni.stored_phone_numbers) != 0:
                    print("\nPhone numbers inserted into the table:")
                    for _ in range(len(pni.stored_phone_numbers)):
                        print (pni.stored_phone_numbers[_])
                else:
                    print("\nNo phone numbers inserted into the table.")
                phone_function = -1

            if phone_function == 3:
                if len(pni.stored_phone_numbers) == 0:
                    print("\nNo phone numbers inserted into the table.")
                    break

                if len(pni.stored_phone_numbers) > 0:
                    print("\nProceed with all phone numbers inserted into the table?\n 1. Yes \n 2. No, let me pick a specific number.")
                    info_function = int(input())

                if info_function == 1:
                    for _ in range(len(pni.stored_phone_numbers)):
                        pni.information(pni.stored_phone_numbers[_])

                if info_function == 2:
                    print("Insert the index of desired phone number:")
                    number = int(input())
                    pni.information(pni.stored_phone_numbers[number])

                phone_function = -1


            if phone_function == 4:
                shutdown = True


    print("\nInto the darkness I descend...")

    # yeeeah, I really need to change it to match/case, that looks ugly as heck

if __name__ == '__main__':
    mantisclaw()